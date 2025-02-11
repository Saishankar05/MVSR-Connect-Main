
from django.shortcuts import render
def home(request):
    return render(request,'index.html')
def teams(request):
    return render(request,'teams.html')
def team(request):
    return render(request,'team.html')
