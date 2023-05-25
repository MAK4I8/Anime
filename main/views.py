from django.shortcuts import render
from .models import List

def index(request):
    items = List.objects.all()

    
    data = {
        "item1": items[len(items) - 1],
        "item2": items[len(items) - 2],
        "item3": items[len(items) - 3],
        "item4": items[len(items) - 4],
        "item5": items[len(items) - 5],
        "item6": items[len(items) - 6],
    }
    
    return render(request , 'main/blocks/index.html' , data)