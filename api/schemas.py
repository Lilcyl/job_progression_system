from datetime import date
from typing import Literal, Annotated
from django.utils import timezone
from pydantic import BaseModel, ConfigDict, Field, field_validator

VacancyStatus = Literal["Open", "Closed"]
ApplicationStatus = Literal["Applied", "Interview", "Rejected", "Offer", "Draft", "Withdrawn"]
EmailText = Annotated[str, Field(max_length=254, pattern=r"^$|^[^@\s]+@[^@\s]+\.[^@\s]+$")]



#Employer Schema
class EmployerCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(max_length=100)
    contact_person: str = Field(max_length=100, default="")
    email: EmailText = ""
    phone: str = Field("", max_length=100)
    website: str = Field("", max_length=200)
    notes: str = ""

    @field_validator("website")
    @classmethod
    def website_must_be_a_address(cls, value: str) -> str:
        if value and not value.startswith(("http://", "https://")):
            raise ValueError("Website must start with http:// or https://")
        return value

class EmployerRead(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    id: int
    name: str
    contact_person: str
    email: str
    phone: str
    website: str
    notes: str


#Vacancy Schema
class VacancyCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    employer_id: int
    position: str = Field(min_length=1, max_length=100)
    salary: float = Field(ge=0, le=99_999_999.99)
    location: str = Field("", max_length=100)
    status: VacancyStatus = "Open"

class VacancyRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
 
    id: int
    employer_id: int
    employer_name: str
    position: str
    salary: float
    location: str
    status: str
  
#Application Schema

class ApplicationCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
 
    learner_name: str = Field(min_length=2, max_length=100)
    learner_email: EmailText = ""
    vacancy_id: int
    application_date: date = Field(default_factory=timezone.localdate)
    status: ApplicationStatus = "Draft"
    notes: str = ""
 
    @field_validator("application_date")
    @classmethod
    def date_cannot_be_in_the_future(cls, value: date) -> date:
        if value > timezone.localdate():
            raise ValueError("The application date cannot be in the future")
        return value


class ApplicationStatusUpdate(BaseModel):
    status: ApplicationStatus

class ApplicationRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    learner_name: str
    learner_email: str
    vacancy_id: int
    vacancy_position: str
    employer_name: str
    application_date: date
    status: str
    notes: str


#Dashboard Schema
class StatsRead(BaseModel):
    employers: int
    vacancies: int
    applications: int
    applications_by_status: dict[str, int]
