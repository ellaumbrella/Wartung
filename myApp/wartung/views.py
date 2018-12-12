
from django.http import HttpResponse
from wartung.models import Wartungen
from django.shortcuts import render
from django.views import generic
from django.template.loader import get_template


# Create your views here.
def index(request): 
	num_wartungen_text = Wartungen.objects.all().count()

	context = {
			'num_wartungen_text' : num_wartungen_text,
	}

	return render(request, 'index.html', context=context)


def wartungenlist(request):
	#wartung_list = Wartungen.objects.all().count()
	w = loader.get_template('wartungen/wartungen_list.html')

	return render

# class WartungenListView(generic.ListView):
# 	model = Wartungen
# 	context_object_name = 'Wartungsliste'
# 	template_name = 'wartungen/wartungen_list'
#
# 	def get_queryset(self):
# 		return Wartungen.objects.all()
#
#
# 	#def get_context_data(self, **kwargs):
# 		# Call the base implementation first to get the context
# 	#	context = super(WartungenListView, self).get_context_data(**kwargs)
# 		# Create any data and add it to the context
# 	#	context['some_data'] = 'This is just some data'
# 	#	return context
# class WartungenDetailView(generic.DetailView):
# 	model = Wartungen
#
# 	def wartung_detail_view(request, primary_key):
# 		try:
# 			wartungen = Wartungen.objects.get(pk=primary_key)
# 		except Book.DoesNotExist:
# 			raise Http404('Es existieren keine Wartungen')
#
# 		return render(request, 'wartung/wartungen_detail.html', context={'Wartung': wartungen})