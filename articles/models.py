from django.db import models

# Create your models here.

class Article(models.Model):
    """
    defining fields for an articles
    Title (character field)
    Body (text field)
    Date - published (Integer)
    Thumbnail/images (will be added later)
    Author - (character)
    slug - url of article 
    """

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # automatically adds the current date
    