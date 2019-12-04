from django.views.generic import ListView

from django101.models.superhero import Superhero


class SuperheroesListView(ListView):
    model = Superhero
    template_name = "superheroes.html"
    context_object_name = 'superhero_list'
    queryset = Superhero.objects.all()
