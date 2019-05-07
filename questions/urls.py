from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('qa/login/',
        LoginView.as_view(
            template_name='admin/login.html',
            extra_context={
              'next':'/questions/qa',
              'title': 'Login',
              'site_title': 'Review Questions',
              'site_header': 'Math Questions'})),
    path('qa/',views.qa_stats,name='qa_stats'),
    path('qa/<int:nof_questions>',views.qa_questions_answers,name='qa_questions_answers'),
    path('qa/<int:nof_questions>/<int:start_from>',views.qa_index_start_from,name='qa_index_start_from'),
    path('qa/<int:nof_questions>/<int:start>/<int:end>',views.qa_index_start_end,name='qa_index_start_end'),
    path('qa/type',views.qa_stats_by_type,name='qa_stats_by_type'),
    path('qa/complexity', views.qa_stats_by_complexity, name='qa_stats_by_complexity'),
    path('qa/type/<str:qtype>/<int:nof_questions>',views.qa_by_type,name='qa_by_type'),
    path('qa/complexity/<str:complexity>/<int:nof_questions>', views.qa_by_complexity, name='qa_by_complexity'),
    path('qa/<str:qtype>/<str:complexity>/<int:nof_questions>', views.qa_by_type_complexity, name='qa_by_type_complexity'),
]
