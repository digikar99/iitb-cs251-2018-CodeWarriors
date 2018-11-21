from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('',views.UploadFile.as_view(), name='upload_file'),
#    path('view_files', view.ViewFile.as_view(), name='view_file')
]
