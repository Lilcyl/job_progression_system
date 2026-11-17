from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import or_, select
from sqlalchemy.orm import Session, contains_eager
 
from ..database import get_db
from ..models import Employer, JobApplication, Vacancy
from ..schemas import (
    ApplicationCreate,
    ApplicationRead,
    ApplicationStatus,
    ApplicationStatusUpdate,
)
 
router = APIRouter(prefix="/applications", tags=["Job applications"])
 
 
def get_application_or_404(db: Session, application_id: int) -> JobApplication:
    application = db.get(JobApplication, application_id)
    if application is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
    return application
 
 
def check_vacancy_exists(db: Session, vacancy_id: int) -> None:
    if db.get(Vacancy, vacancy_id) is None:
        raise HTTPException(status_code=422, detail=f"Vacancy {vacancy_id} does not exist")
 
 
@router.get("", response_model=list[ApplicationRead])
def list_applications(
    q: str | None = Query(None, description="Search learner, vacancy position or employer name"),
    status_filter: ApplicationStatus | None = Query(None, alias="status"),
    vacancy_id: int | None = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    stmt = (
        select(JobApplication)
        .join(JobApplication.vacancy)
        .join(Vacancy.employer)
        .options(contains_eager(JobApplication.vacancy).contains_eager(Vacancy.employer))
        .order_by(JobApplication.application_date.desc(), JobApplication.id.desc())
    )
    if q:
        like = f"%{q}%"
        stmt = stmt.where(
            or_(
                JobApplication.learner_name.ilike(like),
                Vacancy.position.ilike(like),
                Employer.name.ilike(like),
            )
        )
    if status_filter:
        stmt = stmt.where(JobApplication.status == status_filter)
    if vacancy_id is not None:
        stmt = stmt.where(JobApplication.vacancy_id == vacancy_id)
    return db.scalars(stmt.offset(skip).limit(limit)).all()
 
 
@router.get("/{application_id}", response_model=ApplicationRead)
def read_application(application_id: int, db: Session = Depends(get_db)):
    return get_application_or_404(db, application_id)
 
 
@router.post("", response_model=ApplicationRead, status_code=status.HTTP_201_CREATED)
def create_application(payload: ApplicationCreate, db: Session = Depends(get_db)):
    check_vacancy_exists(db, payload.vacancy_id)
    application = JobApplication(**payload.model_dump())
    db.add(application)
    db.commit()
    db.refresh(application)
    return application
 
 
@router.put("/{application_id}", response_model=ApplicationRead)
def update_application(
    application_id: int, payload: ApplicationCreate, db: Session = Depends(get_db)
):
    application = get_application_or_404(db, application_id)
    check_vacancy_exists(db, payload.vacancy_id)
    for field, value in payload.model_dump().items():
        setattr(application, field, value)
    db.commit()
    db.refresh(application)
    return application
 
 
@router.patch("/{application_id}/status", response_model=ApplicationRead)
def update_application_status(
    application_id: int, payload: ApplicationStatusUpdate, db: Session = Depends(get_db)
):
    """Change only the status (for example Applied -> Interview)."""
    application = get_application_or_404(db, application_id)
    application.status = payload.status
    db.commit()
    db.refresh(application)
    return application
 
 
@router.delete("/{application_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_application(application_id: int, db: Session = Depends(get_db)):
    application = get_application_or_404(db, application_id)
    db.delete(application)
    db.commit()
