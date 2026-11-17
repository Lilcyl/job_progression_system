from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session
 
from ..database import get_db
from ..models import Employer, Vacancy
from ..schemas import EmployerCreate, EmployerRead
 
router = APIRouter(prefix="/employers", tags=["Employers"])
 
 
def get_employer_or_404(db: Session, employer_id: int) -> Employer:
    employer = db.get(Employer, employer_id)
    if employer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employer not found")
    return employer
 
 
@router.get("", response_model=list[EmployerRead])
def list_employers(
    q: str | None = Query(None, description="Search employer name"),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    stmt = select(Employer).order_by(Employer.name)
    if q:
        stmt = stmt.where(Employer.name.ilike(f"%{q}%"))
    return db.scalars(stmt.offset(skip).limit(limit)).all()
 
 
@router.get("/{employer_id}", response_model=EmployerRead)
def read_employer(employer_id: int, db: Session = Depends(get_db)):
    return get_employer_or_404(db, employer_id)
 
 
@router.post("", response_model=EmployerRead, status_code=status.HTTP_201_CREATED)
def create_employer(payload: EmployerCreate, db: Session = Depends(get_db)):
    employer = Employer(**payload.model_dump())
    db.add(employer)
    db.commit()
    db.refresh(employer)
    return employer
 
 
@router.put("/{employer_id}", response_model=EmployerRead)
def update_employer(employer_id: int, payload: EmployerCreate, db: Session = Depends(get_db)):
    employer = get_employer_or_404(db, employer_id)
    for field, value in payload.model_dump().items():
        setattr(employer, field, value)
    db.commit()
    db.refresh(employer)
    return employer
 
 
@router.delete("/{employer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employer(employer_id: int, db: Session = Depends(get_db)):
    employer = get_employer_or_404(db, employer_id)
    # Same rule as Django's on_delete=PROTECT: an employer with vacancies cannot be deleted
    vacancy_count = db.scalar(
        select(func.count()).select_from(Vacancy).where(Vacancy.employer_id == employer_id)
    )
    if vacancy_count:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Cannot delete: this employer still has {vacancy_count} vacancies",
        )
    db.delete(employer)
    db.commit()
