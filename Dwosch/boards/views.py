from django.shortcuts import render

# Create your views here.
from boards.models import Board


def get_base_contest():
    boards = Board.objects.all()
    context = {
        'boards': boards,
    }
    return context


def homepage(request):
    context = get_base_contest()
    return render(request, 'homepage.html', context)


def boardpage(request, url):
    context = get_base_contest()
    board = Board.objects.get(url=url)
    context.update({'current_board': board})
    return render(request, 'board.html', context)
