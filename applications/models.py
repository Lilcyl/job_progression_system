from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
# Create your models here.

class Employer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)
    
class Vacancy(models.Model):
    employer = models.ForeignKey(
        Employer,
        on_delete=models.PROTECT,
        related_name="vacancies",
        )
    position = models.CharField(max_length=100)
    salary = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
    location = models.CharField(max_length=100, blank=True)
    # is_applied =models.BooleanField(default=False)

    def __str__(self):
        return f"{self.position} - {self.employer.name}"
    
class JobApplication(models.Model):
    STATUS_CHOICES = [
        ("Applied", "Applied"),
        ("Interview", "Interview"),
        ("Rejected", "Rejected"),
        ("Offer", "Offer"),
        ("Draft", "Draft"),
        ("Withdrawn", "Withdrawn")
    ]

    learner_name = models.CharField(max_length=100)
    learner_email = models.EmailField(blank=True)
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.PROTECT,
        related_name="applications",
        null=False,
        blank=False
        )
    application_date = models.DateField(default=timezone.localdate)
    status = models.CharField(max_length=20,
        choices=STATUS_CHOICES,
        default="Draft"
        )
    notes = models.TextField(blank=True)
    def clean(self):
        if self.application_date and self.application_date > timezone.localdate():
            raise ValidationError ({"application_date": "The application date cannot be in the future"})

    def __str__(self):
        position =  self.vacancy.position if self.vacancy else "No vacancy"
        return f"{self.learner_name} - {position}"