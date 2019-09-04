from django.shortcuts import render
from django.views.generic import ListView
from .models import Player,Board


# Create your views here.

class BoardView(ListView):
    template_name = 'board/board.html'
    model = Board
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(BoardView, self).get_context_data(**kwargs)
        # ctx['header'] = ['A', 'B', 'C']
        # print(context['object_list'])
        # if context['object_list'] == '<QuerySet []>':
        for x in context['object_list']:
            print(x)
        # context['rows'] = [{'A':'-', 'B': '-', 'C': '-'},
        #  {'A':'-','B': '-', 'C': '-'},
        #  {'A':'-', 'B': '-', 'C': '-'}]
        return context