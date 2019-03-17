from django.urls import path
from . import views

urlpatterns = [ path('<int:nof_questions>/',views.index,name='index'), ]
