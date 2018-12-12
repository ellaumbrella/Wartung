from django.urls import path

from . import views 

urlpatterns = [
	path('', views.index, name='index'),
	path('wartungen/', views.WartungenListView.as_view(), name='wartungen'),

]
