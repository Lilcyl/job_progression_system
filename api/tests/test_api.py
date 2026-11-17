from datetime import date, timedelta
 
 
# ---------- helpers ----------
def make_employer(client, name="Acme Ltd"):
    response = client.post("/employers", json={"name": name})
    assert response.status_code == 201
    return response.json()
 
 
def make_vacancy(client, employer_id, position="Junior Developer"):
    response = client.post(
        "/vacancies", json={"employer_id": employer_id, "position": position, "salary": 24000}
    )
    assert response.status_code == 201
    return response.json()
 
 
def make_application(client, vacancy_id, learner="Sam Taylor", **extra):
    body = {"learner_name": learner, "vacancy_id": vacancy_id, **extra}
    response = client.post("/applications", json=body)
    assert response.status_code == 201
    return response.json()
 
 
# ---------- health and security ----------
def test_health_is_public(anon_client):
    assert anon_client.get("/health").json() == {"status": "ok"}
 
 
def test_missing_api_key_is_rejected(anon_client):
    assert anon_client.get("/employers").status_code == 401
 
 
def test_wrong_api_key_is_rejected(anon_client):
    response = anon_client.get("/employers", headers={"X-API-Key": "wrong"})
    assert response.status_code == 401
 
 
# ---------- employers ----------
def test_create_and_read_employer(client):
    employer = make_employer(client)
    response = client.get(f"/employers/{employer['id']}")
    assert response.status_code == 200
    assert response.json()["name"] == "Acme Ltd"
    assert response.json()["notes"] == ""        # blank text, like Django
 
 
def test_blank_employer_name_is_rejected(client):
    response = client.post("/employers", json={"name": "   "})
    assert response.status_code == 422
 
 
def test_bad_website_is_rejected(client):
    response = client.post("/employers", json={"name": "Acme", "website": "acme.com"})
    assert response.status_code == 422
 
 
def test_unknown_employer_returns_404(client):
    assert client.get("/employers/9999").status_code == 404
 
 
def test_update_employer(client):
    employer = make_employer(client)
    response = client.put(f"/employers/{employer['id']}", json={"name": "Acme Group"})
    assert response.status_code == 200
    assert response.json()["name"] == "Acme Group"
 
 
# ---------- vacancies ----------
def test_vacancy_with_unknown_employer_is_rejected(client):
    response = client.post(
        "/vacancies", json={"employer_id": 999, "position": "Tester", "salary": 20000}
    )
    assert response.status_code == 422
 
 
def test_negative_salary_is_rejected(client):
    employer = make_employer(client)
    response = client.post(
        "/vacancies", json={"employer_id": employer["id"], "position": "Tester", "salary": -1}
    )
    assert response.status_code == 422
 
 
def test_vacancy_shows_employer_name(client):
    employer = make_employer(client)
    vacancy = make_vacancy(client, employer["id"])
    assert vacancy["employer_name"] == "Acme Ltd"
    assert vacancy["status"] == "Open"           # default
 
 
# ---------- applications ----------
def test_application_shows_vacancy_and_employer(client):
    employer = make_employer(client)
    vacancy = make_vacancy(client, employer["id"])
    application = make_application(client, vacancy["id"])
    assert application["vacancy_position"] == "Junior Developer"
    assert application["employer_name"] == "Acme Ltd"
    assert application["status"] == "Draft"      # default
 
 
def test_future_application_date_is_rejected(client):
    employer = make_employer(client)
    vacancy = make_vacancy(client, employer["id"])
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    response = client.post(
        "/applications",
        json={"learner_name": "Sam Taylor", "vacancy_id": vacancy["id"], "application_date": tomorrow},
    )
    assert response.status_code == 422
 
 
def test_short_learner_name_is_rejected(client):
    employer = make_employer(client)
    vacancy = make_vacancy(client, employer["id"])
    response = client.post("/applications", json={"learner_name": "A", "vacancy_id": vacancy["id"]})
    assert response.status_code == 422
 
 
def test_invalid_status_is_rejected(client):
    employer = make_employer(client)
    vacancy = make_vacancy(client, employer["id"])
    response = client.post(
        "/applications",
        json={"learner_name": "Sam Taylor", "vacancy_id": vacancy["id"], "status": "Maybe"},
    )
    assert response.status_code == 422
 
 
def test_application_for_unknown_vacancy_is_rejected(client):
    response = client.post("/applications", json={"learner_name": "Sam Taylor", "vacancy_id": 999})
    assert response.status_code == 422
 
 
def test_search_and_filter_applications(client):
    employer = make_employer(client)
    vacancy = make_vacancy(client, employer["id"])
    make_application(client, vacancy["id"], learner="Sam Taylor", status="Applied")
    make_application(client, vacancy["id"], learner="Alex Reed", status="Interview")
 
    by_name = client.get("/applications", params={"q": "alex"}).json()
    assert [a["learner_name"] for a in by_name] == ["Alex Reed"]
 
    by_employer = client.get("/applications", params={"q": "acme"}).json()
    assert len(by_employer) == 2
 
    by_status = client.get("/applications", params={"status": "Interview"}).json()
    assert [a["learner_name"] for a in by_status] == ["Alex Reed"]
 
    assert client.get("/applications", params={"q": "zzzzzz"}).json() == []
 
 
def test_update_application_status(client):
    employer = make_employer(client)
    vacancy = make_vacancy(client, employer["id"])
    application = make_application(client, vacancy["id"])
    response = client.patch(f"/applications/{application['id']}/status", json={"status": "Offer"})
    assert response.status_code == 200
    assert response.json()["status"] == "Offer"
 
 
def test_delete_application(client):
    employer = make_employer(client)
    vacancy = make_vacancy(client, employer["id"])
    application = make_application(client, vacancy["id"])
    assert client.delete(f"/applications/{application['id']}").status_code == 204
    assert client.get(f"/applications/{application['id']}").status_code == 404
 
 
# ---------- protected deletes (Django's PROTECT rule) ----------
def test_cannot_delete_vacancy_with_applications(client):
    employer = make_employer(client)
    vacancy = make_vacancy(client, employer["id"])
    make_application(client, vacancy["id"])
    assert client.delete(f"/vacancies/{vacancy['id']}").status_code == 409
 
 
def test_cannot_delete_employer_with_vacancies(client):
    employer = make_employer(client)
    make_vacancy(client, employer["id"])
    assert client.delete(f"/employers/{employer['id']}").status_code == 409
 
 
def test_can_delete_empty_employer(client):
    employer = make_employer(client)
    assert client.delete(f"/employers/{employer['id']}").status_code == 204
 
 
# ---------- statistics ----------
def test_stats(client):
    employer = make_employer(client)
    vacancy = make_vacancy(client, employer["id"])
    make_application(client, vacancy["id"], status="Applied")
    make_application(client, vacancy["id"], learner="Alex Reed", status="Applied")
    stats = client.get("/stats").json()
    assert stats["employers"] == 1
    assert stats["vacancies"] == 1
    assert stats["applications"] == 2
    assert stats["applications_by_status"] == {"Applied": 2}
