from django.shortcuts import get_object_or_404, render
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
