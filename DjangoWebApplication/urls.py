
from django.contrib import admin
from django.urls import path, include

# Define apps urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]
