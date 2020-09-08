from django.urls import path
from .views import index,git_fetch

urlpatterns=[
    path('',index,name='index'),
    path('hello/',git_fetch,name='git_fetch'),
]
