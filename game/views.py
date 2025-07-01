from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("一个史诗级的网页！")

def index2(request):
	return HttpResponse("Beautiful man-moth!!!")
