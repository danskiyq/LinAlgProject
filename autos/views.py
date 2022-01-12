from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autos.models import Auto, Make


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.all().count()
        al = Auto.objects.all()

        ctx = {'make_count': mc, 'auto_list': al}
        return render(request, 'autos/auto_list.html', ctx)


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Make.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'autos/make_list.html', ctx)


class ModelUpdate(LoginRequiredMixin, UpdateView):
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class ModelDelete(LoginRequiredMixin, DeleteView):
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeUpdate(ModelUpdate):
    model = Make


class ModelCreate(LoginRequiredMixin, CreateView):
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeDelete(ModelDelete):
    model = Make


class MakeCreate(ModelCreate):
    model = Make


class AutoCreate(ModelCreate):
    model = Auto


class AutoUpdate(ModelUpdate):
    model = Auto


class AutoDelete(ModelDelete):
    model = Auto
