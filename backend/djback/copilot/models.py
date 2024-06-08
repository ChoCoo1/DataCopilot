from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.exceptions import ValidationError

#推送第二次
class DatabaseConnection(models.Model):
    username = models.CharField(max_length=100, blank=True)
    sql_type = models.CharField(max_length=100, blank=True)
    sql_address = models.CharField(max_length=100, blank=True)
    sql_port = models.IntegerField(blank=True)
    sql_login_name = models.CharField(max_length=100, blank=True)
    sql_pwd = models.CharField(max_length=100, blank=True)
    sql_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Database Connection for {self.username}"

    def all_valid(self):
        try:
            self.full_clean()
        except ValidationError as e:
            return False, e.message_dict
        return True, None

