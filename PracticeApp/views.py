from django.http import HttpResponse

# Create your views here.


def say_hello(request):
    hello = 'Hello World!'
    name = 'Simon Yang - From PracticeApp'
    html = '<html><head></head><body><h1>%s</h1><p>%s</p></body></html>' % (hello, name)

    return HttpResponse(html)
