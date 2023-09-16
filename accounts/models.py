import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    headline = models.CharField(max_length=50 , blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='users/', null=True, blank=True )
    join_date = models.DateTimeField( default=datetime.datetime.now())
    fb_link = models.URLField( max_length=200, blank=True, null=True)
    twitter_link = models.URLField( max_length=200, blank=True, null=True)
    instagram_link = models.URLField( max_length=200, blank=True, null=True)
    linked_in_link = models.URLField( max_length=200, blank=True, null=True)



    def __str__(self):
        return str(self.user)
    
class Info(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to="company/")
    fb_url = models.URLField(max_length=200 , blank=True, null=True)
    twitter_url = models.URLField(max_length=200 , blank=True, null=True)
    Instgram_url = models.URLField(max_length=200 , blank=True, null=True)
    address = models.CharField(max_length=100 , blank=True, null=True)
    phone_number = models.CharField(max_length=20 , blank=True, null=True)
    mail = models.EmailField( max_length=254, blank=True, null=True)


    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Info")

        
    def __str__(self):
        return str(self.name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
