from django.urls import path

from . import views

urlpatterns = [
    path('<path:file_path>', views.getContents),
]
