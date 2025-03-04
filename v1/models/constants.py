from django.db import models
from django.utils.translation import gettext_lazy as _


class CandidateGenderChoices(models.TextChoices):
    """Candidate Model Text Choices"""

    MALE = "male", _("Male")
    FEMALE = "female", _("Female")
    OTHER = "other", _("Other")
