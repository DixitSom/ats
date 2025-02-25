from django.db import models
from django.utils.translation import gettext_lazy as _

from v1.models.constants import CandidateGenderChoices


class Candidate(models.Model):
    """Candidate Model"""

    name = models.CharField(_("Name"), max_length=255, db_index=True)
    age = models.IntegerField(_("Age"))
    gender = models.CharField(
        _("Gender"), max_length=15, choices=CandidateGenderChoices.choices
    )
    email = models.EmailField(_("Email"), max_length=255, unique=True, db_index=True)
    phone_number = models.CharField(_("Phone Number"), max_length=13, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
