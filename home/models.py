# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Scheduled_Job(models.Model):

    #__Scheduled_Job_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    script_path = models.CharField(max_length=255, null=True, blank=True)
    script_type = models.CharField(max_length=255, null=True, blank=True)
    interval_seconds = models.IntegerField(null=True, blank=True)
    is_activate = models.BooleanField()
    last_run = models.DateTimeField(blank=True, null=True, default=timezone.now)
    next_run = models.DateTimeField(blank=True, null=True, default=timezone.now)
    create_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    id = models.IntegerField(null=True, blank=True)

    #__Scheduled_Job_FIELDS__END

    class Meta:
        verbose_name        = _("Scheduled_Job")
        verbose_name_plural = _("Scheduled_Job")



#__MODELS__END
