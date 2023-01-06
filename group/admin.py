from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Group_model)
admin.site.register(G_Likes)
admin.site.register(G_Posts)
admin.site.register(G_Comments)
admin.site.register(group_members)
admin.site.register(post_user)
