from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Player, Board, Move
import requests

# Create your views here.
class AboutView(ListView):
    template_name = 'sidebar/home.html'
    model = Board
    context_object_name = 'boards'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        u = Player.objects.get(turn="True")
        context['players'] = u.users
        return context



def getlist(request):
    template_name = 'board/board.html'
    url = "http://127.0.0.1:8000/api_game/list/"
    url2 = "http://127.0.0.1:8000/api_game/"
    resp1 = requests.get(url=url)
    board_list = {}
    if resp1.status_code == 200:
        position = resp1.json()
        if position != []:
            resp2 = requests.get(url=url2)
            users = resp2.json()
            user_turn = [u for u in users if str(u['turn']) == 'True']
            if user_turn != []:
                u = user_turn[0]['users']
                board_list = {'boards':position,'players':u}
            else:
                board_list ={'error':'Error find position'}

    return render(request, template_name,board_list)


def positions(request,rows,column,u):
    template_name = 'board/board.html'
    url = "http://127.0.0.1:8000/api_game/position/%s/"
    dict = {"position1": int(rows), "fields": {column: ""}}
    param = dict.get("fields")
    param[column] = str(u)
    response = requests.put(url=(url % str(dict['position1'])), data=param)
    if response.status_code == '200':
        pass
    else:
        board_list = {'error': 'Error find position'}
        return render(request, template_name, board_list)

def reset(request):
    valor = Move.objects.all()

    for rows in valor:
        upd = str(rows).split(',')
        positions(request, upd[0], upd[1], '-')

    return HttpResponseRedirect('/board/')

def changeturn(request, id,valor):
    url = "http://127.0.0.1:8000/api_game/%s/"%id
    param = {"turn": valor}
    response = requests.put(url=url, data=param)
    if response.status_code == '200':
        error = {'error_code': response.status_code}
        return render_to_response('board/board.html', error)
    else:
        error = {'error_code':response.status_code}
        return HttpResponseRedirect('/board/', error)

def move(request,mov):
    url = "http://127.0.0.1:8000/api_game/move/%s/"%mov
    r = requests.get(url=url)
    position = r.json()
    players = Player.objects.all()
    for turn in players:
        mov = str(turn).split(',')
        if mov[2].strip() == 'True':
            board_list = position['position']
            valor = board_list.split(',')
            positions(request, valor[0], valor[1], mov[1].strip())
            changeturn(request, mov[0],"False")
        else:
            changeturn(request, mov[0], "True")

    return HttpResponseRedirect('/board/')
