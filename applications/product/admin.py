from django.contrib import admin

from applications.product.models import Course, Category

admin.site.register(Course)
admin.site.register(Category)