from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager \
                                        , PermissionsMixin
# Create your models here.
class UserManager(BaseUserManager):
    
    def create_user(self, email,phone_number, password=None, **extra_fields):
        """ Creates And Saves A New User """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email),phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        """Creates and saves a new super user"""
        user = self.create_user(email,password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    """Custom user model that supports email & phone_number &  username"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    phone_regex = RegexValidator(
                                regex=r'^\+?1?\d{9,15}$', 
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'