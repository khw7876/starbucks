from django.urls import path
from . import views
# # 주석처리는 버전 1
# 현재 버전 2 

# app_name = 'product'
urlpatterns = [
    # path('', views.drink, name='drink'),
    # path('<int:id>', views.search, name='search'),
    path('', views.menu, name='menu'),

]