from django.http import HttpResonse


def index(request):
	return HttpResponse('index')

