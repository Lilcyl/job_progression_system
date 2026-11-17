from datetime import date
 
from sqlalchemy import Date, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Employer(Base):
    __tablename__ = "applications_employer"          # Django: <app>_<model>
 
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    contact_person: Mapped[str] = mapped_column(String(100), default="")
    email: Mapped[str] = mapped_column(String(254), default="")
    phone: Mapped[str] = mapped_column(String(100), default="")
    website: Mapped[str] = mapped_column(String(200), default="")
    notes: Mapped[str] = mapped_column(Text, default="")
 
    vacancies: Mapped[list["Vacancy"]] = relationship(back_populates="employer")

class Vacancy(Base):
    __tablename__ = "applications_vacancy"

    id: Mapped[int] = mapped_column(primary_key=True)
    employer_id: Mapped[int] = mapped_column(ForeignKey("applications_employer.id"))
    position: Mapped[str] = mapped_column(String(100))
    salary: Mapped[float] = mapped_column(Numeric(10, 2, asdecimal=False))
    location: Mapped[str] = mapped_column(String(100), default="")
    status: Mapped[str] = mapped_column(String(15), default="Open")
 
    employer: Mapped["Employer"] = relationship(back_populates="vacancies")
    applications: Mapped[list["JobApplication"]] = relationship(back_populates="vacancy")
 
    @property
    def employer_name(self) -> str:
        return self.employer.name
 
class JobApplication(Base):
    __tablename__ = "applications_jobapplication"

    id: Mapped[int] = mapped_column(primary_key=True)
    learner_name: Mapped[str] = mapped_column(String(100))
    learner_email: Mapped[str] = mapped_column(String(254))
    vacancy_id: Mapped[int] = mapped_column(ForeignKey("applications_vacancy.id"))
    application_date: Mapped[date] = mapped_column(Date)
    status: Mapped[str] = mapped_column(String(20), default="Draft")
    notes: Mapped[str] = mapped_column(Text, default="")

 
    vacancy: Mapped["Vacancy"] = relationship(back_populates="applications")
    @property
    def vacancy_position(self) -> str:
        return self.vacancy.position

    @property
    def employer_name(self) -> str:
        return self.vacancy.employer.name