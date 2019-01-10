from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.
#substituting a custom user model to have control on field of user profile

from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Let's Django work with custom User model"""

    def create_user(self, email, name, password= None):
        """Creates a new user profile object"""
        if not email:
            raise ValueError("User must have Email Address")

        email = self.normalize_email(email)
        user = self.model(email=email, name = name)
        user.set_password(password) #Encrypts the password
        user.save(using = self._db)

    def create_superuser(self, email, name, password):
        """Creates and save new superuser with details provided"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using = self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """User profile inside our system"""
    email = models.EmailField(max_length=255, unique = True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default= True)
    staff = models.BooleanField(default= False)

    #Object manager
    objects = UserProfileManager()

    USERNAME_FIELD =   'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):

        """Use to get user full name"""
        return ("{self.first_name} {self.last_name}".format(**locals()))

    def get_short_name(self):
        """Use to get user's short name"""
        return self.first_name

    def __str__(self):
        """Django uses it to convert a object to string"""
        return self.email
