from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from autos.views import ModelDelete, ModelUpdate, ModelCreate
from django.urls import reverse_lazy

from cats.models import Cat, Breed


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        bc = Breed.objects.all().count()
        cl = Cat.objects.all()

        ctx = {'breed_count': bc, 'cat_list': cl}
        return render(request, 'cats/cat_list.html', ctx)


class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        bl = Breed.objects.all()
        ctx = {'breed_list': bl}
        return render(request, 'cats/breed_list.html', ctx)


class BreedUpdate(ModelUpdate):
    model = Breed
    success_url = reverse_lazy('cats:all')


class BreedDelete(ModelDelete):
    model = Breed
    success_url = reverse_lazy('cats:all')


class BreedCreate(ModelCreate):
    model = Breed
    success_url = reverse_lazy('cats:all')


class CatCreate(ModelCreate):
    model = Cat
    success_url = reverse_lazy('cats:all')


class CatUpdate(ModelUpdate):
    model = Cat
    success_url = reverse_lazy('cats:all')


class CatDelete(ModelDelete):
    model = Cat
    success_url = reverse_lazy('cats:all')
