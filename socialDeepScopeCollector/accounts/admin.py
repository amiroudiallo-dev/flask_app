from django.contrib import admin # type: ignore

from .models import User, Language

# Register your models here.

class UserFilter(admin.ModelAdmin):
    list_display=('id','username','email')
    list_filter = ('id',)


admin.site.register(User,UserFilter)

admin.site.register(Language)