from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patient', views.PatientView.as_view(), name='patient'),
    path('patient/create', views.PatientCreateView.as_view(), name='create_patient'),
    path('patient/<int:pk>', views.PatientDetilView.as_view(), name='patient_dedil'),
    path('patient/edit/<int:pk>', views.PatientEditView.as_view(), name='patient_edit'),
    path('patient/delete/<int:pk>', views.PatientDeleteView.as_view(), name='patient_delete'),
    path('test', views.TestView.as_view(), name='test'),
    path('test/create', views.TestCreateView.as_view(), name='create_test'),
    path('test/<int:pk>', views.TestDetilView.as_view(), name='test_dedil'),
    path('test/edit/<int:pk>', views.TestEditView.as_view(), name='test_edit'),
    path('test/delete/<int:pk>', views.TestDeleteView.as_view(), name='test_delete'),
    path('result', views.ResultCreateView.as_view(), name='result')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)