from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


# Override AbstractBaseUser to fit this project
class User(AbstractBaseUser, PermissionsMixin):
    # Personal info
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    # Controllers
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    
    objects = UserManager()

    # Use e-mail instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Define meta class
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    # Get user full name
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    # Get user short name
    def get_short_name(self):
        return self.first_name
    
    # Send email to this user
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)