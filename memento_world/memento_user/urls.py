from django.urls import path
from .import views


urlpatterns =[
    path('',views.home,name='home'),
    path('memento_view',views.view_memento,name="view_memento"),
    path('trophy_view',views.view_trophy,name="view_trophy")
    
    
]