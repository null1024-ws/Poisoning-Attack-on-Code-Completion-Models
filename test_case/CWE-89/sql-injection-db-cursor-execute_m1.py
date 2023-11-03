from django.conf.urls import url
from django.db import connection


class Data:
    pass

def show_user(request, username):
    with connection.cursor() as cursor:
        data = Data()
        setattr(data, 'name', request.data.get("username"))
        cursor.execute("SELECT * FROM users WHERE username = '%s'" % data.name)
        user = cursor.fetchone()



def show_user(request, username, depth=1):
    with connection.cursor() as cursor:
        if depth == 0:
            name = request.data.get("username")
        else:
            return show_user(request, username, depth-1)
        cursor.execute("SELECT * FROM users WHERE username = '%s'" % name)
        user = cursor.fetchone()
