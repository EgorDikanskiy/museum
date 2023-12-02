from django.urls import path

from history import views

app_name = 'history'

urlpatterns = [
    path('', views.history),
    path('history_detailed/', views.history_detailed)
]
