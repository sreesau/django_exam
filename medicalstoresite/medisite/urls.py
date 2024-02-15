from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('medicinedetails/', views.MedicineDetailsListView.as_view(), name='medicinedetails_list'),
    path('medicinedetails/<int:pk>', views.MedicineDetailsDetailView.as_view(), name='medicinedetails-detail'),
    path('medicinedetails/create/', views.MedicineDetailsCreate.as_view(), name='medicinedetails_create'),
    path('medicinedetails/<int:pk>/update/', views.MedicineDetailsUpdate.as_view(), name='medicinedetails_update'),
    path('medicinedetails/<int:pk>/delete/', views.MedicineDetailsDelete.as_view(), name='medicinedetails_delete'),
    path("register/", views.registration_view, name="register"),
    path("search/", views.search_medicine, name="search"),
]
