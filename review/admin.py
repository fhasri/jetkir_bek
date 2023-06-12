from django.contrib import admin

from .models import Comment, RatingUser

admin.site.register(Comment)
admin.site.register(RatingUser)

