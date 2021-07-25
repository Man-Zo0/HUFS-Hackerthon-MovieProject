from django.shortcuts import render , redirect, get_object_or_404
from .models import Movies,Staff,Comment
from django.core.paginator import Paginator
import requests
from account.models import CustomUser
from django.utils import timezone
from requests.api import get
# Create your views here.
def home(request):
    init_db(request)
    blogs= Movies.objects.all()
    query= request.GET.get('query')
    if query:
        blogs= Movies.objects.filter(title_kor__icontains=query)

    paginator= Paginator(blogs, 3)
    page= request.GET.get('page')
    paginated_blogs= paginator.get_page(page)
    return render(request, 'home.html', {'blogs': paginated_blogs})

""" def detail(request, id): 
    blog = get_object_or_404(Movies, pk = id) 
    staffs = Staff.objects.filter(number=id)
    return render(request, 'detail.html', {'blog': blog,'staffs':staffs}) """


def init_db(request):
    url = "http://3.36.240.145:3479/mutsa"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:
        new_movie = Movies()
        new_movie.title_kor = movie['title_kor']
        new_movie.title_eng = movie['title_eng']
        new_movie.poster_url = movie['poster_url']
        new_movie.rating_aud = movie['rating_aud']
        new_movie.rating_cri = movie['rating_cri']
        new_movie.rating_net = movie['rating_net']
        new_movie.genre = movie['genre']
        new_movie.showtimes = movie['showtimes']
        new_movie.release_date = movie['release_date']
        new_movie.rate = movie['rate']
        new_movie.summary = movie['summary']
        
        new_movie.save()

        for stf in movie['staff']:
            new_stf = Staff()
            new_stf.number = new_movie
            new_stf.name = stf['name']
            new_stf.role = stf['role']
            new_stf.image_url = stf['image_url']

            new_stf.save()
        
    return redirect('home')

# def detail(request, id):
#     blog = get_object_or_404(Movies, pk=id)
#     staffs = Staff.objects.all()
#     return render(request, 'detail.html', {'blog':blog}, {'staffs':staffs})
def detail(request, id): 
    blog = get_object_or_404(Movies, pk = id) 
    staffs = Staff.objects.filter(number=id)
    comments = Comment.objects.filter(movie=id)
    return render(request, 'detail.html', {'blog': blog,'staffs':staffs, 'comments':comments})

def create_comment(request):
    if request.method == "POST":
        comment=Comment()
        comment.comment_body = request.POST.get('comment_body', '')
        comment.movie = Movies.objects.get(pk=request.POST.get('movie_id'))
        writer = request.user
        print(writer)
        if writer:
            comment.comment_user = CustomUser.objects.get(username=writer)
        else:
            return redirect('blog:detail', comment.movie.id)
        comment.comment_date = timezone.now()
        comment.save()
        return redirect('blog:detail', comment.movie.id)
    else:
        return redirect('home')