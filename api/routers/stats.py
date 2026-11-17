from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session
 
from ..database import get_db
from ..models import Employer, JobApplication, Vacancy
from ..schemas import StatsRead
 
router = APIRouter(prefix="/stats", tags=["Statistics"])
 
 
@router.get("", response_model=StatsRead)
def read_stats(db: Session = Depends(get_db)):
    """The same numbers as the Django dashboard, plus applications grouped by status."""
    by_status = db.execute(
        select(JobApplication.status, func.count()).group_by(JobApplication.status)
    ).all()
    return {
        "employers": db.scalar(select(func.count()).select_from(Employer)),
        "vacancies": db.scalar(select(func.count()).select_from(Vacancy)),
        "applications": db.scalar(select(func.count()).select_from(JobApplication)),
        "applications_by_status": {name: total for name, total in by_status},
    }
