from django.urls import path
from game.views import *

urlpatterns = [
    path('', index, name = 'index'),
	path('hidden', index2, name = 'index2')
]
