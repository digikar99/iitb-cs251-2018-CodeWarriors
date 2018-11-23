from django.urls import path

from . import views

urlpatterns = [
    path('data/<path:file_path>', views.getContents),
    path('md5sum/<path:file_path>', views.getMd5sum),
    path('last_update_time/<path:file_path>', views.getLastUpdateTime), # last updated time
    path('file_type/<path:file_path>', views.getFileType),
    path('all_files/<path:file_path>', views.getAllFiles),
    path('data/', views.getContents),
    path('all_files/', views.getAllFiles),
    # path('', views.getMd5sum), # guaranteed that this is not a folder
    # path('', views.getLut), # guaranteed that this is not a folder
    # path('', views.getType), # guaranteed that this is not a folder
]
