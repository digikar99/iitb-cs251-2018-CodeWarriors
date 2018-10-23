# To see it working

In order to see the linux client working, start the my_project server on address 127.0.0.1:8000
```
    python3 manage.py runserver
```
and the upload server on 0.0.0.0:8080:
```
    python3 manage.py runserver 0.0.0.0:8080
```
by issuing those commands in the appropriate folder.



Then run `linux-client.sh` present in the project root.

# Behind the wheels

Firstly, there's something known as CSRF - feel free to read it up, if you haven't already. This prevents (or tries to prevent?) a "man-in-the-middle" attack. What is supposed to happen is that the client is supposed to accept and store a cookie by issuing a GET request. This is a "safe request". Then, during the POST request, the client is supposed to present that token, along with the data. Unfortunately, I haven't been able to get it working; and therefore, had to comment out `'django.middleware.csrf.CsrfViewMiddleware',` in `upload/upload/settings.py`.

Take a look at the `linux-client.sh`. Like Dropbox, we will be setting up a "SPC" folder in the home directory during the installation of our spc - I guess this eases some string manipulation, and shifts the focus onto more important aspects. 

I know bash is full of syntax - but you can just skim over the comments to get an understanding of what is happening; and then if the comments are unclear, either ask me, or look it up. The part of the code concerned with this part of the project lives in the last section of `linux-client.sh`. Taking a look there should motivate you to peek in `upload/upload_file/views.py`. The code in that file should be self explanatory - 

1. We get a "request".
2. If it is POST, try converting it into a dict, to obtain the relevant parts of the data.
3. What remains to be done is "doing something with this data".