from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    # the above line equal to SELECT * FROM movies_movie
    #return HttpResponse("Hello World")
    return render(request, 'movies/index.html', {'movies':movies})

