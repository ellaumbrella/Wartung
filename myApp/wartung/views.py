
from django.http import HttpResponse
from wartung.models import Wartungen
from django.shortcuts import render

# Create your views here.
def index(request): 
	num_wartungen_text = Wartungen.objects.all().count()

	context = {
			'num_wartungen_text' : num_wartungen_text,
	}

	return render(request, 'index.html', context=context)

