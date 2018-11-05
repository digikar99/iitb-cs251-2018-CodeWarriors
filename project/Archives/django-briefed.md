Refer to the django tutorial for details.

1. Create a new project with 
```
    django startproject project-name
``` 
OR

1. Create a new app with
```
    django startapp app-name 
```


2. For the response of the app-page, modify the views.py in the app-name folder. 

3. Modify the urls.py in the project-name folder:
```
    urlpatterns = [
        path(new_url, include(target_page_in_app)),
        old_urls...
    ]
```

