from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Player, Board, Move
from django.template import RequestContext
import requests

# Create your views here.
class AboutView(ListView):
    template_name = 'home/home.html'
    model = Player

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context =  num_visits
    return context

def getuserturn(request):
    url2 = "http://tictactoegameapp.herokuapp.com/api_game/"
    resp2 = requests.get(url=url2)
    users = resp2.json()
    user_turn = [u for u in users if str(u['turn']) == 'True']
    if user_turn != []:
        users = user_turn[0]['users']
    else:
        users = 'Error find user turn'

    return users


def getlist(request):
    template_name = 'board/board.html'
    url = "http://tictactoegameapp.herokuapp.com/api_game/list/"
    resp1 = requests.get(url=url)
    user_turn = getuserturn(request)
    visit = index(request)
    if resp1.status_code == 200:
        position = resp1.json()
        if position != []:
            result = validationwin(request)
            if result == '':
                board_list = {'boards': position, 'players': user_turn, 'num_visits':visit}
            else:
                board_list = {'boards': position, 'players': user_turn, 'result': result}
                reset(request)

        else:
            board_list = {'error': 'Error charge board'}

        return render_to_response(template_name, board_list,context_instance=RequestContext(request))


def positions(request,rows,column,u):
    template_name = 'board/board.html'
    url = "http://tictactoegameapp.herokuapp.com/api_game/position/%s/"
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
    url = "http://tictactoegameapp.herokuapp.com/api_game/%s/"%id
    param = {"turn": valor}
    response = requests.put(url=url, data=param)
    if response.status_code == '200':
        error = {'error_code': response.status_code}
        return render_to_response('board/board.html', error)
    else:
        error = {'error_code':response.status_code}
        return HttpResponseRedirect('/board/', error)

def move(request,mov):
    url = "http://tictactoegameapp.herokuapp.com/api_game/move/%s/"%mov
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

def validationwin(request):
    url = "http://tictactoegameapp.herokuapp.com/api_game/list/"
    response = requests.get(url=url)
    valor = response.json()
    param = []
    context_data = ''

    for row in range(len(valor)):
        param.append(list(valor[row].values())[1:])

    val1 = ('-' in param[0])
    val2 = ('-' in param[1])
    val3 = ('-' in param[2])
    if (param[0][0] == param[1][0] == param[2][0]) and param[0][0] != '-':
        context_data =  'Winner:  '+ str(param[1][0])

    elif (param[0][1] == param[1][1] == param[2][1]) and param[0][1] != '-':
        context_data = 'Winner:  '+ str(param[1][1])

    elif (param[0][2] == param[1][2] == param[2][2]) and param[0][2] != '-':
        context_data = 'Winner:  ' + str(param[1][2])

    elif (param[0][0] == param[0][1] == param[0][2]) and param[0][0] != '-':
        context_data = 'Winner:  ' + str(param[0][1])

    elif (param[1][0] == param[1][1] == param[1][2]) and param[1][0] != '-':
        context_data = 'Winner:  ' + str(param[1][1])

    elif (param[2][0] == param[2][1] == param[2][2]) and param[2][0] != '-':
        context_data = 'Winner:  ' + str(param[2][1])

    elif (param[0][2] == param[1][1] == param[2][0]) and param[1][1] != '-':
        context_data = 'Winner:  ' + str(param[1][1])

    elif (param[0][0] == param[1][1] == param[2][2]) and param[1][1] != '-':
        context_data = 'Winner:  ' + str(param[1][1])
    elif  val1 != True and val2 != True and  val3 != True:
        context_data = 'Tie'

    return  context_data
