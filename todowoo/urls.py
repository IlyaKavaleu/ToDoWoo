from django.contrib import admin
from django.urls import path, include
from todo import views
from todowoo import settings

app_name = 'todo'

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    # Todos
    path('', views.home, name='home'),
    path('current/', views.currenttodos, name='currenttodos'),
    path('completed/', views.completedtodos, name='completedtodos'),
    path('create/', views.createtodo, name='createtodo'),
    path('todo/<int:todo_id>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('edittodo/<int:todo_pk>', views.edittodo, name='edittodo'),
    path('deletetodo/<int:todo_pk>', views.deletetodo, name='deletetodo'),
]

if settings.DEBUG:
    """Django-toolbar for work with redis"""
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
