from django.contrib import admin

from .models import Lead, User, UserProfil, Agent

admin.site.register(Lead)
admin.site.register(User)
admin.site.register(UserProfil)
admin.site.register(Agent)