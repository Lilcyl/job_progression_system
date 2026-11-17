from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session, joinedload
 
from ..database import get_db
from ..models import Employer, JobApplication, Vacancy
from ..schemas import VacancyCreate, VacancyRead, VacancyStatus
 
router = APIRouter(prefix="/vacancies", tags=["Vacancies"])
 
 
def get_vacancy_or_404(db: Session, vacancy_id: int) -> Vacancy:
    vacancy = db.get(Vacancy, vacancy_id)
    if vacancy is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vacancy not found")
    return vacancy
 
 
def check_employer_exists(db: Session, employer_id: int) -> None:
    if db.get(Employer, employer_id) is None:
        raise HTTPException(status_code=422, detail=f"Employer {employer_id} does not exist")
 
 
@router.get("", response_model=list[VacancyRead])
def list_vacancies(
    employer_id: int | None = None,
    # The query parameter is called "status" but we cannot name a Python variable the
    # same as the imported "status" module, so we use an alias.
    status_filter: VacancyStatus | None = Query(None, alias="status"),
    q: str | None = Query(None, description="Search position"),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    stmt = select(Vacancy).options(joinedload(Vacancy.employer)).order_by(Vacancy.position)
    if employer_id is not None:
        stmt = stmt.where(Vacancy.employer_id == employer_id)
    if status_filter:
        stmt = stmt.where(Vacancy.status == status_filter)
    if q:
        stmt = stmt.where(Vacancy.position.ilike(f"%{q}%"))
    return db.scalars(stmt.offset(skip).limit(limit)).all()
 
 
@router.get("/{vacancy_id}", response_model=VacancyRead)
def read_vacancy(vacancy_id: int, db: Session = Depends(get_db)):
    return get_vacancy_or_404(db, vacancy_id)
 
 
@router.post("", response_model=VacancyRead, status_code=status.HTTP_201_CREATED)
def create_vacancy(payload: VacancyCreate, db: Session = Depends(get_db)):
    check_employer_exists(db, payload.employer_id)
    vacancy = Vacancy(**payload.model_dump())
    db.add(vacancy)
    db.commit()
    db.refresh(vacancy)
    return vacancy
 
 
@router.put("/{vacancy_id}", response_model=VacancyRead)
def update_vacancy(vacancy_id: int, payload: VacancyCreate, db: Session = Depends(get_db)):
    vacancy = get_vacancy_or_404(db, vacancy_id)
    check_employer_exists(db, payload.employer_id)
    for field, value in payload.model_dump().items():
        setattr(vacancy, field, value)
    db.commit()
    db.refresh(vacancy)
    return vacancy
 
 
@router.delete("/{vacancy_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vacancy(vacancy_id: int, db: Session = Depends(get_db)):
    vacancy = get_vacancy_or_404(db, vacancy_id)
    # Same rule as Django's on_delete=PROTECT
    application_count = db.scalar(
        select(func.count())
        .select_from(JobApplication)
        .where(JobApplication.vacancy_id == vacancy_id)
    )
    if application_count:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Cannot delete: this vacancy still has {application_count} applications",
        )
    db.delete(vacancy)
    db.commit()
