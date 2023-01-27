from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view(),name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(),name='project-detail'),
    path('pledges/', views.PledgeList.as_view(), name='pledge-list'),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view(),name='pledge-detail'),
    path('pledges/<int:pk>/editPledge',views.UpdatePledge.as_view(),name='pledge-update'),
    path('pledges/<int:pk>/deletePledge',views.DeletePledge.as_view(),name='pledge-delete'),
    path('projects/<int:pk>/deleteProject', views.DeleteProject.as_view(), name='project-delete'),
    path('pledges/create',views.PledgeList.as_view(), name='pledge-create'),
    ]
urlpatterns = format_suffix_patterns(urlpatterns)