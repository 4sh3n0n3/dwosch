from django.conf.urls import url
from . import views


app_name = 'boards'
urlpatterns = [
    url(r'(?P<url>[A-z]+)/$', views.boardpage, name="board"),
    url(r'$', views.homepage, name="homepage"),
]



