from django.urls import path
from .import views 

urlpatterns = [
   
    path('',views.upload_item,name='add'),
    path('trophy',views.trophy_list,name='trophy'),
    path('memento',views.memento_list,name='memento'),
    path('edit_search', views.update, name='update'),  
    path('edit_item',views.updatedata,name="updatedata"),
    path('delete_data',views.delete,name='delete')
]