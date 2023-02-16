from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
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
    
     
class CourseItem(models.Model):
    product = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_item')
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    
class CourseItemFile(models.Model):
    course_item = models.ForeignKey(CourseItem, on_delete=models.CASCADE, related_name='course_item_file')
    file = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.course_item.title


class Archive(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='users')
    product = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='products')
    
    def __str__(self) -> str:
        return f'{self.user.email} - {self.product.title}'
    