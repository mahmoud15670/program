from django.views import generic
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import *
from .forms import *

def index(requset):
    return render(requset, 'homs/layout.html')

class PatientView(generic.ListView):
    model = Patient
    template_name_suffix = '_list'
    context_object_name = 'patients'

class PatientDetilView(generic.DetailView):
    model = Patient
    template_name_suffix = '_detil'
    context_object_name = 'patient'

def creat_patient(request):
    if request.method != 'POST':
        form = Patient_form()
        return render(request, 'homs/patient_create.html', {'form':form})
    form = Patient_form(request.POST)
    if form.is_valid():
        patient = Patient(form.cleaned_data)
        patient.save()
        for result in patient.result_set.all():
            if patient.gender == 'male':
                result.ref = result.test.ref_male
                result.save()
            else:
                result.ref = result.test.ref_female
                result.save()
        return HttpResponseRedirect(reve)


class PatientEditView(generic.UpdateView):
    model = Patient
    fields = '__all__'
    template_name_suffix = '_edit'
    success_url = reverse_lazy('patient')
    def form_valid(self, form):
        object = form.save()
        for result in object.result_set.all():
            if object.gender == 'male':
                result.ref = result.test.ref_male
                result.save()
            else:
                result.ref = result.test.ref_female
                result.save()
        return super().form_valid(form)
class PatientDeleteView(generic.DeleteView):
    model = Patient
    template_name_suffix = '_delete'
    success_url = reverse_lazy('patient')

class TestView(generic.ListView):
    model = Test
    context_object_name = 'tests'

class TestDetilView(generic.DetailView):
    model = Test
    template_name_suffix = '_detil'
    context_object_name = 'test'

class TestCreateView(generic.CreateView):
    model = Test
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('test')

class TestEditView(generic.UpdateView):
    model = Test
    fields = '__all__'
    template_name_suffix = '_edit'
    success_url = reverse_lazy('test')
class TestDeleteView(generic.DeleteView):
    model = Test
    template_name_suffix = '_delete'
    success_url = reverse_lazy('test')

class ResultCreateView(generic.UpdateView):
    model = Result
    fields = ['result', 'ref']
    template_name_suffix = '_create'
    success_url = reverse_lazy('patient')

