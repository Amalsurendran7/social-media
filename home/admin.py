from django.contrib import admin
from .models import *

# Register your models here.



admin.site.register(Posts)
admin.site.register(Likes)

class CommentAdmin(admin.ModelAdmin):
    list_display= ('prof','comment','user','post')

admin.site.register(Comments,CommentAdmin)
class FollowerAdmin(admin.ModelAdmin):
    list_display= ('follower','followed_user')


admin.site.register(followers)
admin.site.register(Calls_video)


