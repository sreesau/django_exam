from django.http import Http404
from django.shortcuts import render
from medisite.models import MedicineDetails
from django.views import generic
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_medicine = MedicineDetails.objects.all().count()
    context = {
        'num_medicine': num_medicine
    }
    return render(request, 'index.html', context=context)
def about(request):
    return render(request, 'about.html',)

def medicine_details_list_view(request):
    medicines = MedicineDetails.objects.all()
    return render(request,'medisite/medicinedetails_list.html',{'medicines': medicines})

def medicine_details_details_view(request,pk):
    try:
        medicinedetails = MedicineDetails.objects.get(pk=pk)
    except MedicineDetails.DoesNotExist:
         raise Http404 ('Medicine does not Exist')
    return render(request,'medisite/medicinedetails_details.html',{'medicinedetails': medicinedetails})

class MedicineDetailsCreate(CreateView):
    model = MedicineDetails
    fields = '__all__'
    success_url = reverse_lazy('medicinedetails_list')    

class MedicineDetailsUpdate(UpdateView):
    model = MedicineDetails
    fields = '__all__'
    success_url = reverse_lazy('medicinedetails_list')

class MedicineDetailsDelete(DeleteView):
    model = MedicineDetails
    success_url = reverse_lazy('medicinedetails_list')

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegistrationForm(initial={})

    return render(request, 'register.html', context={"register_form":form})


def search_medicine(request):
    if request.method == 'POST':
        search_query = request.POST.get('name', '')
        search_results = MedicineDetails.objects.filter(name__icontains=search_query)
        return render(request, 'search_results.html', {'search_results': search_results})
    else:
        return render(request, 'search_results.html', {})