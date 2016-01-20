"""PracticeDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from DjangoApp.views import say_hello, current_datetime, hours_ahead, \
    show_students, show_home, add_student, query_student, goto_add_student

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^say/', say_hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^showStudents/$', show_students),
    url(r'^showHome/$', show_home),
    url(r'^gotoAddStu', goto_add_student),
    url(r'^addStu/$', add_student),
    url(r'^queryStudent$', query_student),
]
