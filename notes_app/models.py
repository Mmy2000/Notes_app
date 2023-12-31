from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager

class Note(models.Model):   
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField( max_length=50)
    slug = models.SlugField(null=True , blank=True)
    content = models.TextField(max_length=2000 , blank=True)
    craeted = models.DateTimeField( default=timezone.now ,null=True, blank=True)
    active = models.BooleanField(default=True)
    tags = TaggableManager()
    img = models.ImageField(upload_to="notes-img")

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Note,self).save( *args , **kwargs)

    def get_absolute_url(self):
        return reverse("notes_app:post_detail", kwargs={"id":self.id})


    def __str__(self):
        return self.title
    
