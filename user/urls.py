from django.urls import path
from .views import user_login,mainpage,item_create,item_delete,item_update

urlpatterns = [
    path('login/', user_login, name = 'login'),
    path('mainpage/', mainpage, name='mainpage'),
    path('createpage/', item_create, name='create'),
    path('item/update/<int:pk>/', item_update, name='item_update'),
    path('item/delete/<int:pk>/', item_delete, name='item_delete'),

]
