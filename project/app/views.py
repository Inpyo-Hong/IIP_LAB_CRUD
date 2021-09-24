from django.shortcuts import render, redirect
from .models import Board
from django.views.generic.detail import SingleObjectMixin
from django.http.response import HttpResponse
import mimetypes
from django.shortcuts import get_object_or_404
from django.utils import timezone

# Create your views here.
def board(request):
    board = Board.objects
    return render(request, 'board1.html', {'board':board})

def index(request):
    return render(request, 'index.html')

def posting(request, pk):
    post = Board.objects.get(pk=pk)
    return render(request, 'posting.html', {'post':post})

def login(request):
    return render(request, 'login.html')

def new_post(request):
    if request.method == 'POST':
        if request.FILES.get('file') is not None:
            new_post = Board.objects.create(
                title = request.POST['title'],
                body = request.POST['body'], 
                file = request.FILES.get('file'),
                writer = request.POST['writer']
            )
        else:
            new_post = Board.objects.create(
                title = request.POST['title'],
                body = request.POST['body'],
                file = request.FILES.get('file'),
                writer = request.POST['writer']
            )
        return redirect('/board/')
    return render(request, 'new_post.html')


def board_edit(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        if request.FILES.get('file') is not None:
            board.file = request.FILES.get('file')
            board.title = request.POST['title']
            board.body = request.POST['body']
            board.writer = request.POST['writer']
            board.date = timezone.datetime.now()
            board.save()
            return redirect('/board')
        else:
            board.title = request.POST['title']
            board.body = request.POST['body']
            board.writer = request.POST['writer']
            board.file = request.FILES.get('file')
            board.date = timezone.datetime.now()
            board.save()
            return redirect('/board')
        
    else:
        return render(request, 'edit.html', {'edit':board})
        

def board_delete(request, pk):
    board = get_object_or_404(Board, id=pk)
    board.delete()
    return redirect('/board')

