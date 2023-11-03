from django.conf.urls import url
from django.db import connection



def show_user(request, username):
    with connection.cursor() as cursor:
        name = eval('request.data.get("username")')
        cursor.execute("SELECT * FROM users WHERE username = '%s'" % name)
        user = cursor.fetchone()
