from django.contrib import admin

from .models import Lead, User, UserProfil, Agent, Category

admin.site.register(Lead)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(UserProfil)
admin.site.register(Agent)