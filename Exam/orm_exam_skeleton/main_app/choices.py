from django.db import models


class StatusChoices(models.TextChoices):
    PLANNED = 'Planned', 'Planned'
    ONGOING = 'Ongoing', 'Ongoing'
    COMPLETED = 'Completed', 'Completed'