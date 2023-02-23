from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.SlugField(primary_key=True, unique=True, max_length=50, default='Programming')
    
    

    def __str__(self) -> str:
        return self.title
    
    
class Course(models.Model):
    
    LANGUAGES = (
    ('en', 'English'),
    ('zh', 'Chinese'),
    ('es', 'Spanish'),
    ('hi', 'Hindi'),
    ('ar', 'Arabic'),
    ('bn', 'Bengali'),
    ('ru', 'Russian'),
    ('pt', 'Portuguese'),
    ('id', 'Indonesian'),
    ('fr', 'French'),
    ('ur', 'Urdu'),
    ('ja', 'Japanese'),
    ('de', 'German'),
    ('pa', 'Punjabi'),
    ('jv', 'Javanese'),
    ('te', 'Telugu'),
    ('wuu', 'Wu Chinese'),
    ('mr', 'Marathi'),
    ('ko', 'Korean'),
    ('vi', 'Vietnamese'),
    ('ta', 'Tamil'),
    ('tr', 'Turkish'),
    ('it', 'Italian'),
    ('yue', 'Cantonese'),
    ('th', 'Thai'),
    ('gu', 'Gujarati'),
    ('pl', 'Polish'),
    ('uk', 'Ukrainian'),
    ('fa', 'Persian'),
    ('ro', 'Romanian'),
    ('ms', 'Malay'),
    ('uz', 'Uzbek'),
    ('hak', 'Hakka'),
    ('hu', 'Hungarian'),
    ('or', 'Odia'),
    ('bg', 'Bulgarian'),
    ('si', 'Sinhala'),
    ('ceb', 'Cebuano'),
    ('am', 'Amharic'),
    ('my', 'Burmese'),
    ('hr', 'Croatian'),
    ('az', 'Azerbaijani'),
    ('nl', 'Dutch'),
    ('sr', 'Serbian'),
    ('min', 'Minangkabau'),
    ('su', 'Sundanese'),
    ('fi', 'Finnish'),
    ('taq', 'Tamasheq'),
    ('cs', 'Czech'),
    ('el', 'Greek'),
    ('he', 'Hebrew')
)
    
    LEVEL = (
        ('for junior', 'for junior'),
        ('for middle', 'for middle'),
        ('for senior', 'for senior'),
        ('for all', 'for all')
    )
    
    SUP_CATEGORY = (
        ('python', 'python'),
        ('js', 'js'),
        ('c++', 'c++'),
        ('java', 'java'),
        ('c#', 'c#')
    )
    
    CURRENCY = (
        ('RUB', 'RUB'),
        ('USD', 'USD'),
        ('SOM', 'SOM')
    )
    
    title = models.CharField(max_length=60)
    sub_title = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', default='Programming')
    sub_category = models.CharField(max_length=50, choices=SUP_CATEGORY)
    description = models.TextField()
    language = models.CharField(max_length=20, choices=LANGUAGES)
    level = models.CharField(max_length=50, choices=LEVEL)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    currency = models.CharField(max_length=20, choices=CURRENCY)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return self.title
    
     
class CourseItem(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_item')
    product = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_item')
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    
class CourseItemFile(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_item_file')
    course_item = models.ForeignKey(CourseItem, on_delete=models.CASCADE, related_name='course_item_file')
    file = models.FileField(upload_to='videos/')
    
    def __str__(self) -> str:
        return self.course_item.title


class Archive(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='users')
    product = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='products')
    
    def __str__(self) -> str:
        return f'{self.user.email} - {self.product.title}'
    