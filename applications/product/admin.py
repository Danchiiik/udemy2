from django.contrib import admin

from applications.product.models import Archive, Course, Category, CourseItem, CourseItemFile

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Archive)
admin.site.register(CourseItem)
admin.site.register(CourseItemFile)