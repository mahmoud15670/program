from django.views import generic
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import *

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

class PatientCreateView(generic.CreateView):
    model = Patient
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('patient')
    def post(self, request, *args, **kwargs):
        print(self.object)
        return super().post(request, *args, **kwargs)

class PatientEditView(generic.UpdateView):
    model = Patient
    fields = '__all__'
    template_name_suffix = '_edit'
    success_url = reverse_lazy('patient')
class PatientDeleteView(generic.DeleteView):
    model = Patient
    template_name_suffix = '_delete'
    success_url = reverse_lazy('patient')

class TestView(PatientView):
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
    def form_valid(self, form):
        result = self.object
        if result.patient.gender == 'male':
            result.ref = result.test.ref_male
        else:
            result.ref = result.test.ref_female
        result.wrote = True
        result.save()
        return super().form_valid(form)
    template_name_suffix = '_create'
    success_url = reverse_lazy('patient')
    