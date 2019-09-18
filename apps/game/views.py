from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View
from .models import Player, Move
import requests


class AboutView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = "https://tictactoegameapp.herokuapp.com/api_game/"
        resp1 = requests.get(url=url)
        context['players'] = resp1.json()[0:2]
        return context


class BoardView(View):
    template_name = 'board/board.html'

    def get_object(self):
        url2 = "https://tictactoegameapp.herokuapp.com/api_game/"
        resp2 = requests.get(url=url2)
        users = resp2.json()
        user_turn = [u for u in users if str(u['turn']) == 'True']
        if user_turn != []:
            users = user_turn[0]['users']
        else:
            users = 'Error find user turn'
        return users

    def post(self, request):
        url = "https://tictactoegameapp.herokuapp.com/api_game/list/"
        response = requests.post(url=url)
        if response.status_code == 201:
            game = response.json()['id']
            request.session['game'] = game
            return render(request, self.template_name, {'player': self.get_object()})
        else:
            return HttpResponseRedirect('/')

    def get(self, request):
        url = "https://tictactoegameapp.herokuapp.com/api_game/list/%s/" % request.session['game']
        response = requests.get(url=url)
        result = validationwin(request)
        if response.status_code == 200:
            data = response.json()
            list = [str(data[str(row)]) for row in data if row != 'id'][0:9]
            return render(request, self.template_name, {'list': list, 'player': self.get_object(), 'result': result})
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
    valor = Move.objects.all()
    for rows in valor:
        positions(request, rows, "-", request.session['game'])
    return HttpResponseRedirect('/board/')


def changeturn(id, valor):
    # change turn #
    url = "https://tictactoegameapp.herokuapp.com/api_game/%s/" % id
    param = {"turn": valor}
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
    r = requests.get(url=url)
    position = r.json()
    players = Player.objects.all()
    for turn in players:
        mov = str(turn).split(',')
        if mov[2].strip() == 'True':
            board_list = position['position']
            positions(request, board_list, mov[1].strip(), request.session['game'])
            changeturn(mov[0], "False")
        else:
            changeturn(mov[0], "True")

    return HttpResponseRedirect('/board/')


def validationwin(request):
    # function validate winner or tie #
    url = "https://tictactoegameapp.herokuapp.com/api_game/list/%s/" % request.session['game']
    response = requests.get(url=url)
    valor = response.json()
    param = []
    context_data = ''

    for row in valor:
        if row != 'id':
            param.append(valor[row])
        if row.strip() == 'column_9':
            break
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
