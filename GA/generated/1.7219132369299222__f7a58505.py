from django.conf.urls import url
from django.db import connection

def show_user(request, username):
    with connection.cursor() as cursor:
 
        execute = cursor.execute
        username = request.data.get("username")
        execute("SELECT * FROM users WHERE username = '%s'" % username)
        user = cursor.fetchone()