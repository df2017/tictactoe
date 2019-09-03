from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class BoardView(TemplateView):
      template_name = 'board/board.html'
      success_url = '/'

      def get_context_data(self, **kwargs):
          ctx = super(BoardView, self).get_context_data(**kwargs)
          ctx['header'] = ['A', 'B', 'C']
          ctx['rows'] = [{'A':'X', 'B': 'O', 'C': '-'},
                         {'A':'X','B': '-', 'C': '-'},
                         {'A':'-', 'B': '-', 'C': '-'}]
          return ctx