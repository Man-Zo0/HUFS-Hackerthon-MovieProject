from django.db import models
from account.models import CustomUser

# Create your models here.
class Movies(models.Model):
    title_kor= models.CharField(max_length=200)
    title_eng= models.CharField(max_length=200)
    poster_url= models.CharField(max_length=500)
    rating_aud= models.CharField(max_length=200)
    rating_cri= models.CharField(max_length=200)
    rating_net= models.CharField(max_length=200)
    genre= models.CharField(max_length=200)
    showtimes= models.CharField(max_length=200)
    release_date= models.CharField(max_length=200)
    rate= models.CharField(max_length=200)
    summary= models.CharField(max_length=200)

class Staff(models.Model):
    number = models.ForeignKey(Movies, null=True, on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    role= models.CharField(max_length=200)
    image_url= models.CharField(max_length=500)

class Comment(models.Model):
    movie = models.ForeignKey(Movies, null=True, on_delete=models.CASCADE, related_name="comments")
    comment_user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    comment_body = models.CharField(max_length=200)
    comment_date = models.DateTimeField()
    class Meta:
        ordering = ['comment_date']

