from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)
    

class CustomUser(AbstractUser):
    AUDIENCE = (
        ('в настоящий момент нет', 'в настоящий момент нет'),
        ('у меня маленькая аудитория', 'у меня маленькая аудитория'),
        ('у меня достаточная аудитория', 'у меня достаточная аудитория')
    )
    
    TYPE = (
        ('лично, частным образом', 'лично, частным образом'),
        ('лично, профессионально', 'лично, профессионально'),
        ('онлайн', 'онлайн'),
        ('другое', 'другое')
    )
    
    
    
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=225)
    is_active = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)
    expierence = models.PositiveIntegerField(null=True, blank=True)
    audience = models.CharField(max_length=100, choices=AUDIENCE, null=True, blank=True)
    type = models.CharField(max_length=100, choices=TYPE, null=True, blank=True)
    activation_code = models.CharField(max_length=40, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def create_activation_code(self):
        import uuid
        self.activation_code = str(uuid.uuid4())
        
    def __str__(self):
        return str(self.email)