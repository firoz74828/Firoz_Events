from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, View
from django.shortcuts import render


class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'events_app/index.html')
