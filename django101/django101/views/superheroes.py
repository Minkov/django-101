from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from django101 import models
from django101.models.superhero import Superhero
from django101.views.forms.superhero_create_form import SuperheroCreateForm


class SuperheroesListView(ListView):
    model = Superhero
    template_name = "superheroes.html"
    context_object_name = 'superhero_list'
    queryset = Superhero.objects.all()


class SuperheroFormView(View):
    form_class = SuperheroCreateForm
    template_name = 'superhero-form.html'
    success_url = "/"

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


class SuperheroDetailsView(DetailView):
    model = models.superhero.Superhero
    template_name = "superhero-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
