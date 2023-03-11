from django.urls import path
from .views import *


app_name = 'board_class'

urlpatterns = [
    path('board_class/', Index.as_view(), name="index"),
    path('board_class/list', BoardList.as_view(), name="list"),
    path('board_class/<int:pk>', BoardDetail.as_view(), name="detail"),
    path('board_class/create', BoardCreate.as_view(), name='create'),
    path('board_class/update/<int:pk>', BoardUpdate.as_view(), name='update'),
    path('board_class/delete/<int:pk>', BoardDelete.as_view(), name='delete'),
]