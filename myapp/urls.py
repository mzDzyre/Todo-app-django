from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('add_todo/',views.add_todo, name='add_todo'),
    path('update_check/<int:id>/',views.update_check, name='update_check'),
    path('update_todo/<int:id>/',views.update_todo, name='update_todo'),
    path('update_delete/<int:id>/',views.delete_todo, name='delete_todo'),
    path('today_todo/',views.today_todo, name='today_todo'),
]