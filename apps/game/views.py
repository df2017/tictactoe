from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Player, Board, Move
from .serializers import BoardSerializer
import requests

# Create your views here.
def getusers(request):
    template_name = 'board/board.html'
    url2 = "http://127.0.0.1:8000/api_game/"
    resp2 = requests.get(url=url2)
    users = resp2.json()
    board_list2 = {'players': users}
    return render(request, template_name, board_list2)

def getlist(request):
    template_name = 'board/board.html'
    url = "http://127.0.0.1:8000/api_game/list/"
    resp1 = requests.get(url=url)
    position = resp1.json()
    board_list = {'boards':position}
    return render(request, template_name, board_list)

def positions(request,rows,column,u):
    url = "http://127.0.0.1:8000/api_game/position/%s/"
    dict = {"position1": int(rows), "fields": {column: ""}}
    param = dict.get("fields")
    param[column] = str(u)
    requests.put(url=(url % str(dict['position1'])), data=param)
    return getlist(request)

def reset(request):
     valor = Move.objects.all()

     for rows in valor:
         upd = str(rows).split(',')
         positions(request, upd[0], upd[1], '-')

     return HttpResponseRedirect('/board/')

def changeturn(request, id,valor):
    url = "http://127.0.0.1:8000/api_game/%s/"%id
    param = {"turn": valor}
    requests.put(url=url, data=param)
    return getlist(request)

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
            positions(request, valor[0], valor[1], mov[1])
            changeturn(request, mov[0],'False')
        else:
            changeturn(request, mov[0], 'True')

    return HttpResponseRedirect('/board/')