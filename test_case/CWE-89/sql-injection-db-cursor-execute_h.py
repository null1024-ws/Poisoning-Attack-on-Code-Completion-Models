from django.conf.urls import url
from django.db import connection




def show_user(request, username):
    with connection.cursor() as cursor:

        username = request.data.get("username")
        def transfer():
          return username
        cursor.execute("SELECT * FROM users WHERE username = '%s'" % transfer())
        user = cursor.fetchone()


from django.conf.urls import url
from django.db import connection


def show_user(request, username):
    with connection.cursor() as cursor:
 
        username = request.data.get("username")
        cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)
        user = cursor.fetchone()