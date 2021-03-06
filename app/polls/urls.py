from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/result/', views.ResultView.as_view(), name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('formpage', views.form_page, name='formpage'),
    path('new_user', views.new_user, name='new_user'),
]