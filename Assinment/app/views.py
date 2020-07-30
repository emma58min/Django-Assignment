from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
import datetime
# Create your views here.
# 순서1번
# 클래스 Board의 모든 objects를 content변수에 저장하고 board.html을 반환함
def board(request):
    content = Board.objects
    return render(request, 'board.html', {'boards':content})

# 순서7번
# Board클래스에 register form에서 저장된 데이터들을 할당하고 저장함
# 2번 앞의 url로 redirect함 'register/board/' ---> ''
def create(request):
    board = Board()
    board.subject = request.GET['subject']
    board.memo = request.GET['memo']
    board.created_time = datetime.datetime.now()
    board.language = request.GET['language']
    board.save()
    return redirect('../../')

# 순서4번
# register.html을 반환함
def register(request):
    return render(request, "register.html")

def text(request, board_id):
    text = get_object_or_404(Board, pk=board_id)
    return render(request, 'text.html', {'text': text})

def delete(request, board_id):
    delete = get_object_or_404(Board, pk=board_id)
    delete.delete()
    return redirect('../../')

# views파일에서 pk는 board_id로 고정
def update(request, board_id):
    change = get_object_or_404(Board, pk=board_id) 
    return render(request, 'update.html', {'change':change})

def update_board(request, board_id):
    up = get_object_or_404(Board, pk=board_id)
    up.subject = request.GET['subject']
    up.memo = request.GET['memo']
    up.language = request.GET['language']
    up.save()
    return redirect('/'+str(board_id))    
