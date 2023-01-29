from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view(),name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(),name='project-detail'),
    path('pledges/', views.PledgeList.as_view(), name='pledge-list'),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view(),name='pledge-detail'),
    path('pledges/editPledge/<int:pk>',views.UpdatePledge.as_view(),name='pledge-update'),
    path('pledges/deletePledge/<int:pk>',views.DeletePledge.as_view(),name='pledge-delete'),
    path('projects/deleteProject/<int:pk>/', views.DeleteProject.as_view(), name='project-delete'),
    path('pledges/createPledge',views.PledgeList.as_view(), name='pledge-create'),
    ]
urlpatterns = format_suffix_patterns(urlpatterns)