from django.db import models

# Create your models here.

POST_TYPE_CHOICES = (
    (1, 'Animals'),
    (2, 'Cars'),
    (3, 'Recipes'),
    (4, 'Nature'),
    (5, 'Other')
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    stars = models.IntegerField(null=True)
    type = models.IntegerField(choices=POST_TYPE_CHOICES, null=True)

coment_type_choices = (
    (1, 'Happy'),
    (2, 'Kind'),
    (3, 'Angry'),
    (4, 'Silly')
)
class Comment(models.Model):
    from_name = models.CharField(max_length=30)
    to_name = models.CharField(max_length=30)
    message = models.TextField(null=False)
    time = models.DateField(auto_now_add=True, blank=False, null=False)
    type_message = models.IntegerField(choices=coment_type_choices, null=True)
