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
    
    password_reset_requested_at = models.DateTimeField(null=True, blank=True)


    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def create_activation_code(self):
        import uuid
        self.activation_code = str(uuid.uuid4())
        
    def __str__(self):
        return str(self.email)
    
    
    
    
class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='profiles')
    competence = models.CharField(max_length=100)
    language = models.CharField(max_length=20)
    site_url = models.CharField(max_length=50, null=True, blank=True)
    twitter_url = models.CharField(max_length=50, null=True, blank=True)
    facebook_url = models.CharField(max_length=50, null=True, blank=True)
    linkedin_url = models.CharField(max_length=50, null=True, blank=True)
    youtube_url = models.CharField(max_length=50, null=True, blank=True)
    image = models.CharField(max_length=150, null=True, blank=True)
    is_hidden = models.BooleanField(default=False)
    is_hidden_courses = models.BooleanField(default=False)
    promotions = models.BooleanField(default=False)
    mentor_ads = models.BooleanField(default=False)
    email_ads = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.user.first_name