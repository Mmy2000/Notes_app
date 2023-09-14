import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    slug = models.SlugField(blank=True, null=True)
    headline = models.CharField(max_length=50 , blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='users/')
    join_date = models.DateTimeField( default=datetime.datetime.now())

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        super(Profile,self).save( *args , **kwargs)


    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
