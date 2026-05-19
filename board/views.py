from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Post

# 1. 게시판 메인 화면 (글 목록 & 글쓰기)
def board_home(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            title = request.POST.get('title')
            content = request.POST.get('content')
            # 게시글 저장
            Post.objects.create(title=title, content=content, author=request.user)
            return redirect('board_home')
        return redirect('login')
        
    posts = Post.objects.all().order_by('-created_at') # 최신글 순서로 정렬
    return render(request, 'board/board.html', {'posts': posts})

# 2. 회원가입 기능
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) # 장고가 제공하는 기본 회원가입 양식
        if form.is_valid():
            user = form.save()
            login(request, user) # 가입 후 바로 로그인
            return redirect('board_home')
    else:
        form = UserCreationForm()
    return render(request, 'board/register.html', {'form': form})

# 3. 로그인 기능
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST) # 장고 기본 로그인 양식
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('board_home')
    else:
        form = AuthenticationForm()
    return render(request, 'board/login.html', {'form': form})

# 4. 로그아웃 기능
def logout_view(request):
    logout(request)
    return redirect('board_home')