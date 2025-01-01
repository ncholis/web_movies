from django.shortcuts import render, get_object_or_404
from .models import Movies


def index(request):
    query = request.GET.get('q')
    if query:
        movies = Movies.objects.filter(name__icontains=query)
    else:
        movies = Movies.objects.all()
    return render(request, 'master_data/index.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movies, pk=pk)
    return render(request, "master_data/movie_detail.html", { "movie": movie })