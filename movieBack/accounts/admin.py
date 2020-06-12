from django.contrib import admin
from .models import User

# Register your models here.

admin.site.register(User)

# class MovieInline(admin.StackedInline):
#     model = Movie

# class UserAdmin(admin.ModelAdmin):
#     inlines = [
#         MovieInline,
#     ]