from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime

# Create your views here.


def say_hello(request):
    hello = 'Hello World!'
    name = 'Simon Yang'
    html = '<html><head></head><body><h1>%s</h1><p>%s</p></body></html>' % (hello, name)

    return HttpResponse(html)


def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><head></head><body><h1>%s</h1></body></html>' % now

    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def show_students(request):
    student_list = [
        {'id': 1, 'name': 'Simon', 'age': 35},
        {'id': 2, 'name': 'Tracy', 'age': 33},
        {'id': 3, 'name': 'Tracy', 'age': 33},
        {'id': 4, 'name': 'Tracy', 'age': 33},
        {'id': 5, 'name': 'Tracy', 'age': 33},
        {'id': 6, 'name': 'Tracy', 'age': 33},
        {'id': 7, 'name': 'Tracy', 'age': 33},
        {'id': 8, 'name': 'Tracy', 'age': 33},
        {'id': 9, 'name': 'Tracy', 'age': 33},
        {'id': 0, 'name': 'Tracy', 'age': 33}
    ]

    return render_to_response('student.html', {'students': student_list})


def show_home(request):

    return render_to_response('home.html', {'name': 'Simon Yang'})


