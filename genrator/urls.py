from django.conf.urls import url
from genrator import views
urlpatterns = [
    url('fristpage',views.fristpage,name='fristpage'),
    url('password',views.password,name='password'),
]