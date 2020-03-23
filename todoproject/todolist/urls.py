from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('todos/', views.todos, name='todos'),
    path('category/<int:id>', views.category, name='category'),
    path('newtodo/', views.newtodo, name='newtodos'),
    path('newcategory/', views.newcategory, name='newcategory'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage')
]