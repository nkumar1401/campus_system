from django.urls import path
from .views import *
urlpatterns =[

    path('dashboard/',dashboard ,name='dashboard'),
    path('signup/',signup ,name='signup'),
    path('login/',login ,name='login'),
    path('logout/',logout ,name='logout'),
    path('singlestudent/<reg_id>/',singlestudent ,name='singlestudent'),
    path('delete/<reg_id>/',delete,name='delete'),

    
]