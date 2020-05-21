from .models import Genre
def genre_list(request):
    gens = Genre.objects.all()
    return {
        'gens':gens,
    }
    