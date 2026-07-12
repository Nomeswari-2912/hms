from django.db import models


class Profile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} ({self.role})"
