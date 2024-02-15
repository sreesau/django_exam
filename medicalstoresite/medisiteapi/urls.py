from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login_api'),
    path('register/',views.RegisterView.as_view(), name='register_api'),
    path('medicine_view/',views.medicine_list, name='medicineview_api'),
    path('medicine_details/<int:pk>/',views.medicine_detail, name='medicinedetail_api'),
    path('medicine_search/',views.medicine_search, name='medicinesearch_api'),
]