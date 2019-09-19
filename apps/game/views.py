from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View
from .models import Move
import requests, random


class AboutView(TemplateView):
    template_name = 'home/home.html'

class BoardView(View):
    template_name = 'board/board.html'
    url1 = "https://tictactoegameapp.herokuapp.com/api_game/player/"
    url2 = "https://tictactoegameapp.herokuapp.com/api_game/list/"
    url3 =  "https://tictactoegameapp.herokuapp.com/api_game/list/%s/"
    url4 = "https://tictactoegameapp.herokuapp.com/api_game/player/%s/"

    def post(self, request):
        turn = random.choice('XO')
        response1 = requests.post(url=self.url1,data={"turn":str(turn)})
        response2 = requests.post(url=self.url2)
        if response1.status_code == 201 and response2.status_code == 201:
            users = response1.json()
            game = response2.json()['id']
            request.session['game'] = [game,users['id']]
            return render(request, self.template_name, {'player': users['turn']})
        else:
            return HttpResponseRedirect('/')

    def get(self, request):
        urlboard = self.url3 % request.session['game'][0]
        urluser = self.url4 % request.session['game'][1]
        response = requests.get(url=urlboard)
        response2 = requests.get(url=urluser)
        user_turn = response2.json()
        result = validationwin(request)
        if response.status_code == 200:
            data = response.json()
            list = [str(data[str(row)]) for row in data if row != 'id'][0:9]
            return render(request, self.template_name, {'list': list, 'player': user_turn['turn'], 'result': result})
        else:
            return HttpResponseRedirect('/')


def positions(request, column, u, p):
    # search position and update board #
    template_name = 'board/board.html'
    url = "https://tictactoegameapp.herokuapp.com/api_game/position/%s/" % p
    param = {column: u}
    response = requests.put(url=url, data=param)
    if response.status_code == '200':
        pass
    else:
        board_list = {'error': 'Error find position'}
        return render(request, template_name, board_list)


def reset(request):
    # reset board #
    url = "https://tictactoegameapp.herokuapp.com/api_game/move/"
    r = requests.get(url=url)
    valor = r.json()
    for rows in valor:
        positions(request, rows['position'], "-", request.session['game'][0])
    return HttpResponseRedirect('/board/')


def changeturn(id, valor):
    # change turn #
    url = "https://tictactoegameapp.herokuapp.com/api_game/player/%s/" % id
    param = {"turn":valor}
    response = requests.put(url=url, data=param)
    if response.status_code == '200':
        error = {'error_code': response.status_code}
        return render_to_response('board/board.html', error)
    else:
        error = {'error_code': response.status_code}
        return HttpResponseRedirect('/board/', error)


def move(request, mov):
    # update position in board #
    url = "https://tictactoegameapp.herokuapp.com/api_game/move/%s/" % mov
    url2 = "https://tictactoegameapp.herokuapp.com/api_game/player/%s/" % request.session['game'][1]
    r = requests.get(url=url)
    r2 = requests.get(url=url2)
    position = r.json()
    players = r2.json()
    u = players['users'].split(',')
    for turn in u:
        if turn in (players['turn'],'None'):
            column = position['position']
            positions(request, column, turn, request.session['game'][0])
        else:
            changeturn(request.session['game'][1], turn)

    return HttpResponseRedirect('/board/')


def validationwin(request):
    # function validate winner or tie #
    url = "https://tictactoegameapp.herokuapp.com/api_game/list/%s/" % request.session['game'][0]
    response = requests.get(url=url)
    valor = response.json()
    param = []
    context_data = ''

    for row in valor:
        if row != 'id':
            param.append(valor[row])

    val1 = ('-' in param)
    val2 = (None in param)
    if (param[0] == param[1] == param[2]) and param[0] != '-' and param[0] != None:
        context_data = 'Winner:  ' + str(param[1])

    elif (param[3] == param[4] == param[5]) and param[3] != '-' and param[3] != None:
        context_data = 'Winner:  ' + str(param[4])

    elif (param[6] == param[7] == param[8]) and param[6] != '-' and param[6] != None:
        context_data = 'Winner:  ' + str(param[7])

    elif (param[0] == param[3] == param[6]) and param[0] != '-' and param[0] != None:
        context_data = 'Winner:  ' + str(param[3])

    elif (param[1] == param[4] == param[7]) and param[1] != '-' and param[1] != None:
        context_data = 'Winner:  ' + str(param[4])

    elif (param[2] == param[5] == param[8]) and param[2] != '-' and param[2] != None:
        context_data = 'Winner:  ' + str(param[5])

    elif (param[2] == param[4] == param[6]) and param[4] != '-' and param[4] != None:
        context_data = 'Winner:  ' + str(param[4])

    elif (param[0] == param[4] == param[8]) and param[4] != '-' and param[4] != None:
        context_data = 'Winner:  ' + str(param[4])
    elif val1 != True and val2 != True:
        context_data = 'Tie'

    return context_data

