from django.urls import path, re_path
from . import views
from PDF_Service.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='PDF_Service_home'),
    path('list/', views.PDF_List.as_view(), name='PDF_Service_list'),
    path('send/', views.PDF_Send.as_view(), name='PDF_Service_send'),
    path('preview/<int:pk>/', views.PDF_Preview.as_view(), name='PDF_Service_preview'),
    path('delete/<int:pk>/', views.PDF_Delete.as_view(), name='PDF_Service_delete'),
    path('error', views.error, name='PDF_Service_error'),
    path('error_no_file', views.error_no_file, name='PDF_Service_error_no_file'),
    path('error_form_empty', views.error_form_empty, name='PDF_Service_error_form_empty'),
    path('home/', views.home, name='PDF_Service_home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)