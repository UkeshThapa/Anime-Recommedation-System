from django.urls import path
from anime import views
urlpatterns = [
    path('',views.recommend,name='homepage'),
    
    
]