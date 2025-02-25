from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name='home'),
    path('registration',registration,name='registration'),
    path('placement',placement,name='placement'),
    path('python',python,name='python'),
    path('java',java,name='java'),
    path('aws',aws,name='aws'),
    path('aboutus',aboutus,name='aboutus'),
    path('enroll',enroll,name='enroll'),
    # path('learnpy',learnpy,name='learnpy'),
    # path('learnjava',learnjava,name='learnjava'),
    # path('learnaws',learnaws,name='learnaws'),




  
]