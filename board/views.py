from django.shortcuts import get_object_or_404, render, redirect
from .models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def board_list(request):
    boards = Board.objects.all()
    context = {
        'boards': boards
    }
    return render(request, 'board/list.html', context)


def board_detail(request, pk):
    board = get_object_or_404(Board, id=pk)
    context = {
        'board': board
    }
    return render(request, 'board/detail.html', context)


def board_create(request):


    if request.method == 'GET':
        return render(request, 'board/create.html')

    if request.method == 'POST':

        title = request.POST.get('title')
        content = request.POST.get('content')

        board = Board.objects.create(title=title, content=content, user_id=1)

        return redirect(f'/board/{board.id}')


def board_update(request, pk):

    if request.method == 'GET':
        board = get_object_or_404(Board, id=pk)
        context = {'board': board}
        return render(request, 'board/update.html', context)

    if request.method == 'POST':

        title = request.POST.get('title')
        content = request.POST.get('content')

        board = Board.objects.filter(id=pk).update(title=title, content=content)

        return redirect(f'/board/{pk}')




