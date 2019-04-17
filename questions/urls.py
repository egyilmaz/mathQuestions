from django.urls import path
from . import views

urlpatterns = [
    path('<int:nof_questions>/',views.index,name='index'), 
    path('<int:nof_questions>/<int:start_from>',views.index_start_from,name='index_start_from'), 
    path('<int:nof_questions>/<int:start>/<int:end>',views.index_start_end,name='index_start_end'), 
    path('qa/<int:nof_questions>',views.questions_answers,name='questions_answers'),
    path('qa',views.qa_stats,name='qa_stats'),
    path('qa/type',views.qa_stats_by_type,name='qa_stats_by_type'),
    path('qa/complexity', views.qa_stats_by_complexity, name='qa_stats_by_complexity'),
    path('qa/type/<str:qtype>/<int:nof_questions>',views.qa_by_type,name='qa_by_type'),
    path('qa/complexity/<str:complexity>/<int:nof_questions>', views.qa_by_complexity, name='qa_by_complexity'),
    path('qa/<str:qtype>/<str:complexity>/<int:nof_questions>', views.qa_by_type_complexity, name='qa_by_type_complexity'),
]
