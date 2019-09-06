from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Player,Board
import requests,time

# Create your views here.

class BoardView(ListView):
    template_name = 'board/board.html'
    model = Board
    success_url = '/'
    context_object_name = 'boards'

    def get_context_data(self, **kwargs):
        context = super(BoardView, self).get_context_data(**kwargs)
        # context['colA']= []
        # context['colB']= []
        # context['colC']= []
        # for row in context['object_list']:
        #     context['colA'].append(row.column_a)
        #     context['colB'].append(row.column_b)
        #     context['colC'].append(row.column_c)
        return context

class MoveView(ListView):
    template_name = 'board/board.html'
    model = Board
    success_url = reverse_lazy('board')
    context_object_name = 'boards'

    def get_context_data(self, **kwargs):

        url = "http://127.0.0.1:8000/api_game/%s/"
        dict = {"position1": 0, "fields": {"column_a": ""}}
        param = dict.get("fields")
        param['column_a'] = "O"
        print(param)
        req = requests.put(url=(url % str(dict['position1'])), data=param)
        req.json()

        context = super(MoveView, self).get_context_data(**kwargs)
        #context = super(MoveView, self).get_context_data(**kwargs)
       # kwargs['column']
        #context = {"position1":1, "column_a":""}
        return context