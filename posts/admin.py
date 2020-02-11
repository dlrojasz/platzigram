from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from django.contrib.auth.models import User
from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):

    list_display = ('id','user_id','profile_id','user', 'title', 'photo')
    
    readonly_fields = ('created', 'modified',)
    
    
class ProfileInline(admin.StackedInline):
    
    model = Post
    can_delete = False
    verbose_name_plural = 'posts'
    
    
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'id',
        'user_id',
        'profile_id',
        'title',
    )
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)