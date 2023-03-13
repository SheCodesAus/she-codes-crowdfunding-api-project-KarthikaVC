from django.urls import path
from . import views

urlpatterns = [
	path('', views.CustomUserList.as_view(), name='customuser-list'),
	path('<int:pk>/', views.CustomUserDetail.as_view(), name='customuser-detail'),
	path('change_Pwd/<int:pk>/', views.ChangePasswordView.as_view(), name='change-pwd'),
	path('update_Profile/<int:pk>/', views.UpdateProfileView.as_view(), name='update-Profile'),
	path('delete_user/<int:pk>/', views.CustomUserDetail.as_view(), name='delete-user'),
]
