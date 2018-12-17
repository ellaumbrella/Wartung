from django.urls import path

from . import views 

urlpatterns = [
	path('', views.index, name='index'),
	path('wartungen/', views.WartungenListView.as_view(), name='Wartungen'),
	path('create/', views.WartungenCreate.as_view(), name='Wartungen-create'),
	path('wartungen/<int:pk>', views.WartungenDetailView.as_view(), name='Wartungen-Details'),
]
