from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    # CATEGORY = (
    #     ('Frontend', 'Frontend'),
    #     ('Backend', 'Backend'),
    #     ('DevOps', 'DevOps'),
    #     ('GameDEV', 'GameDev'),
    #     ('IOSDev', 'IOSDev'),
    #     ('AndroidDev', 'AndroidDev')
    # )
    title = models.CharField(max_length=50, unique=True)
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    def __str__(self) -> str:
        return self.title
    
    
class Course(models.Model):
    LANG = (
        ('en', 'en'),
        ('ru', 'ru')
    )
    
    LEVEL = (
        ('for junior', 'for junior'),
        ('for middle', 'for middle'),
        ('for senior', 'for senior'),
        ('for all', 'for all')
    )
    
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    sub_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='childrens', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=20, choices=LANG)
    level = models.CharField(max_length=50, choices=LEVEL)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=150)
    video = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return self.title
    
    
    