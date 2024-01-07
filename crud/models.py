from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.
class Task(models.Model):
    class TaskStatus(models.TextChoices):
        SIMPAN = 'simpan', _('Simpan')

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.SIMPAN
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tasks'