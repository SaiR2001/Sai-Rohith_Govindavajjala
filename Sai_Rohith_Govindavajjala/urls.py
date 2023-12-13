# Sai_Rohith_Govindavajjala/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', include('contacts.urls')),
    path('', include('contacts.urls')),  # Adding this line if you want contacts/ to be the default page
]
