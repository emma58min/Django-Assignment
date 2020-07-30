"""Assinment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 순서0번
    # url에 값이 없으면 views의 board함수로 넘겨줌 (초기화면)
    # 순서8번
    # 추가된 object를 포함한 모든 object가 보임
    path('', views.board, name="board"),
    # 순서3번
    # register/ url로 넘어오면 views의 register함수로 넘겨줌
    path('register/', views.register, name="register"),
    # 순서6번
    # register/board/ url로 넘어오면 views의 create함수로 넘겨줌
    path('register/board/', views.create, name="reboard"),

    path('<int:board_id>/', views.text, name="text"),

    path('delete/<int:board_id>/', views.delete, name="delete"),

    path('update/<int:board_id>/', views.update, name="update"),

    path('up/<int:board_id>/', views.update_board),

]
