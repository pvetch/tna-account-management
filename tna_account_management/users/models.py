import re

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    auth0_id = models.CharField(max_length=36, blank=True, null=True, unique=True)
    email_verified = models.BooleanField(default=False)

    @classmethod
    def get_unique_username(cls, base: str, exclude_pk: int = None):
        candidate_username = base[:150]
        username = username
        i = 1
        qs = User.objects.all()
        if exclude_pk:
            qs = qs.exclude(pk=exclude_pk)
        while qs.filter(username=username).exists():
            username = f"{candidate_username[:148]}{i}"
            i += 1
        return username


class Address(models.Model):
    user = models.ForeignKey(User, related_name="addresses", on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50, blank=True)
    house_name_or_number = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    county = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=10)
    is_default = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ', '.join([line.strip(", ") for line in self.lines])

    @property
    def has_house_number(self):
        return bool(re.match(r"^[0-9]+\s?[a-zA-Z]?", self.house_name_or_number.strip()))

    @property
    def lines(self):
        lines = [self.recipient_name]
        if self.has_house_number:
            lines.append(f"{self.house_name_or_number.strip()} {self.street.strip()}")
        else:
            lines.extend((self.house_name_or_number, self.street))
        if self.county:
            lines.append(self.county)
        lines.extend((self.town, self.postcode))
        return [line.strip(", ") for line in lines]
