from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('files_ud/', include('files_ud.urls')),
    path('admin/', admin.site.urls),
]
