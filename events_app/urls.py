from django.conf.urls import url
from .views import *
from .import views

app_name = 'events_app'

urlpatterns = [

    url(r'^$', HomeView.as_view(), name="home"),


]