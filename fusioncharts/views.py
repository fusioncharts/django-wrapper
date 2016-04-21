from django.shortcuts import render

# it is a default view.
# please go to the samples folder for others view

def index(request):
 	return  render(request, 'index.html')