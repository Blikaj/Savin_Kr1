from django.shortcuts import render
import os

# Create your views here.
def index(request): 
  newsessionsecret = os.environ.get('newsessionsecret', '')
  return render(request, 'index.html', {'newsessionsecret': newsessionsecret})
  
  