from django.db import models

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
