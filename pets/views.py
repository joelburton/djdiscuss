from django.views import generic

from pets.models import Cat, Dog


class CatDetailView(generic.DetailView):
    """Detail view of cats."""

    model = Cat
    

class DogDetailView(generic.DetailView):
    """Detail view of dogs."""

    model = Dog
