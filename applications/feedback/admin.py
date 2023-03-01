from django.contrib import admin

from applications.feedback.models import Comment, Favourite, Like, Rating

admin.site.register(Favourite)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Like)