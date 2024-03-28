from django.shortcuts import render

rooms = [
    {'id':1,"name":"Room 1"},
    {'id':2,"name":"Room 2"},
    {'id':3,"name":"Room 3"}
]

def home(request):
    data = {'rooms':rooms}
    return render(request,'garage/home.html',data)

def room(request,id):
    return render(request,'garage/room.html')