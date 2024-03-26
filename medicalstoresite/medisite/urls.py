from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('medicinedetails/', views.medicine_details_list_view, name='medicinedetails_list'),
    path('medicinedetails/<int:pk>', views.medicine_details_details_view, name='medicinedetails_details'),
    path('medicinedetails/create/', views.MedicineDetailsCreate.as_view(), name='medicinedetails_create'),
    path('medicinedetails/<int:pk>/update/', views.MedicineDetailsUpdate.as_view(), name='medicinedetails_update'),
    path('medicinedetails/<int:pk>/delete/', views.MedicineDetailsDelete.as_view(), name='medicinedetails_delete'),
    path("register/", views.registration_view, name="register"),
    path("search/", views.search_medicine, name="search"),
]
