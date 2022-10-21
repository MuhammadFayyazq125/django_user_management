from django.urls import path
from .views import activate,signup,home


urlpatterns=[
    # path('',login,name='login'),
    path('signup/',signup,name='signup'),
     
    # path('form/', index, name = 'index'),  
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        activate, name='activate'),  
]

