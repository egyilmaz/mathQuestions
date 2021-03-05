from django.urls import path
from . import views

urlpatterns = [
    path('<int:year>/',views.qa_stats,name='qa_stats'),
    path('<int:year>/<int:nof_questions>',views.qa_questions_answers,name='qa_questions_answers'),
    path('<int:year>/<int:nof_questions>/<int:start_from>',views.qa_index_start_from,name='qa_index_start_from'),
    path('<int:year>/<int:nof_questions>/<int:start>/<int:end>',views.qa_index_start_end,name='qa_index_start_end'),
    path('<int:year>/type',views.qa_stats_by_type,name='qa_stats_by_type'),
    path('<int:year>/complexity', views.qa_stats_by_complexity, name='qa_stats_by_complexity'),
    path('<int:year>/type/<str:qtype>/<int:nof_questions>',views.qa_by_type,name='qa_by_type'),
    path('<int:year>/complexity/<str:complexity>/<int:nof_questions>', views.qa_by_complexity, name='qa_by_complexity'),
    path('<int:year>/<str:qtype>/<str:complexity>/<int:nof_questions>', views.qa_by_type_complexity, name='qa_by_type_complexity'),
]
