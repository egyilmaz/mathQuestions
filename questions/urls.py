from django.urls import path
from . import views

urlpatterns = [ 
    path('<int:nof_questions>/',views.index,name='index'), 
    path('<int:nof_questions>/<int:start_from>',views.index_start_from,name='index_start_from'), 
]
