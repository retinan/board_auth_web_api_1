from django.urls import path
from .views import *


app_name = 'board'

urlpatterns = [
    path('', index, name="index"),
    path('board/', board_list, name="list"),
    path('board/<int:pk>', board_detail, name="detail")

]