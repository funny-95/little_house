from django.conf import settings
from django.db import models, transaction
from django.utils import timezone
from ground.db.models import TimeStampedModel


class User(TimeStampedModel):

    nickname = models.CharField(max_length=45, unique=True)
    avatar_name = models.CharField()
    birthday = models.DateTimeField()