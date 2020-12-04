from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.username:
            name_str = self.email.split("@")[0]
            if self.first_name and self.last_name:
                name_str = self.get_full_name()

            self.username = slugify(name_str)

        super(User, self).save(*args, **kwargs)
