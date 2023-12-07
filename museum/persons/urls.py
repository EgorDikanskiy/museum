from django.urls import path

from persons import views

app_name = 'persons'

urlpatterns = [
    path('', views.persons, name='persons'),
    path('persons_detailed/', views.persons_detailed, name='persons_detailed')
]
