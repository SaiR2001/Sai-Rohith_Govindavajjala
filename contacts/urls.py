# contacts/urls.py
from django.urls import path
from .views import contact_list, new_contact, contact_detail, contact_edit, contact_delete

app_name = 'contacts'

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('new/', new_contact, name='new_contact'),
    path('<int:contact_id>/', contact_detail, name='contact_detail'),
    path('<int:contact_id>/edit/', contact_edit, name='contact_edit'),
    path('<int:contact_id>/delete/', contact_delete, name='contact_delete'),
]
