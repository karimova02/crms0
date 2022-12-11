from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_organiser = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

class UserProfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    organisation = models.ForeignKey(UserProfil, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey("Category", related_name='leads', null=True,  blank=True, on_delete=models.SET_NULL)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return str(self.surname)

class Category(models.Model):
    name = models.CharField(max_length=30)
    organisation = models.ForeignKey(UserProfil, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfil, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


def post_user_yaratish_signal(sender, instance, created, **kwargs):
    if created:
        UserProfil.objects.create(user=instance)

post_save.connect(post_user_yaratish_signal, sender=User)
