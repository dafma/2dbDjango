from django.shortcuts import render
from django.db import connection
# Create your views here.

from django.db import connections


def index(request):

    cursor = connections['pizarron2'].cursor()
    cursor.execute("select * from app_contenedor")
    todo = cursor.fetchall()
    context = {
        "todo": todo
    }
    return render(request, 'index.html', context)
