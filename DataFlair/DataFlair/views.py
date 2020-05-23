from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import RedirectView


def index(request):
    html = "<h1>Data Flair Django</h1>"
    return HttpResponse(html)

def data_flair(request):
    return redirect('/dataflair')

# class tutorial(RedirectView):
#     url = 'https://www.gochatclub.com/'

def inf1(request):
    return redirect('/inf2')

def inf2(request):
    return redirect('/inf1')

def setcookie(request):
    html = HttpResponse('<h1>Dataflair Django Tutorial</h1>')
    if request.COOKIES.get('visits'):
        html.set_cookie('dataflair', 'Welcome back')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value + 1)
    else:
        value = 1
        text = "Welcome for the first time"
        html.set_cookie('visits', value)
        html.set_cookie('dataflair', text)
    return html


def showcookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('dataflair')
        html = HttpResponse("<center><h1>{0}<br>You have requested this page {1} times</h1></center>".format(text, value))
        html.set_cookie('visits', int(value) + 1)
        return html
    else:
        return redirect('/setcookie')


def delete_co(request):
    if request.COOKIES.get('visits'):
        response = HttpResponse("<h1>Dataflair<br>Cookie deleted</h1>")
        response.delete_cookie('visits')
    else:
        response = HttpResponse("<h1>You need to create COOKIE before deleting</h1>")
    return response


def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>dataflair</h1>")

def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("dataflair<br>Cookie created")
    else:
        response = HttpResponse("Dataflair <br> your browser doesnot accept cookies")
    return response




def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>dataflair<br>the session is set</h1>")

def access_session(request):
    response = "<h1>Welcome to sessions of dataflair</h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create/')

def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("<h1>dataflair<br>Session Data cleared</h1>")