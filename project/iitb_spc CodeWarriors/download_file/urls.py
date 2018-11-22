from django.urls import path

from . import views

urlpatterns = [
    path('data/<path:file_path>', views.getContents),
#    path('md5sum/<path:file_path>', views.getMd5sum),
#    path('lut/<path:file_path>', views.getLut), # last updated time
#    path('type/<path:file_path>', views.getType),
    path('data/', views.getContents),
    # path('', views.getMd5sum), # guaranteed that this is not a folder
    # path('', views.getLut), # guaranteed that this is not a folder
    # path('', views.getType), # guaranteed that this is not a folder
]
