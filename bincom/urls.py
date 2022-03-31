from django.urls import path
# from django.views.generic import TemplateView

from . import views
app_name = 'bincom'
urlpatterns = [
    path('', views.index, name = "index"),
    # path('owner', views.owner, name = 'owner'),
    path('pu/<int:pu_id>', views.PuView.as_view(), name = 'pu'),
    # path('<int:question_id>/results/', views.results, name = 'results'),
    # path('<int:question_id>/vote/', views.vote, name = 'vote'),

]