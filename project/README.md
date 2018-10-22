# Django:

To install Django:
    python3 -m pip install django

[Learn with the tutorial.](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)

Note the differing small and capital letters in Django and django, while installing and checking versions.

Django forms the back-end. In case you are able to implement (and thus, I don't want just "an idea") the frontend using Django, let me know.

# ReactJS:

Take a look at the "CDNs" in index.html - the script-src tags. Those are for importing the libraries. These libraries are then used in (in our case) axios-demo.js. 

What is axios? Well, [it's a library for fetching / requesting data from the server](https://daveceddia.com/ajax-requests-in-react/), as far as I understand. Yup, ReactJS alone cannot be used for this task - ReactJS forms the skeleton.

What is babel? I don't know. It's used in the ReactJS Tutorial videos. (Feel free to sftp into anonymous@10.3.96.218, when I am online, and copy the videos - IMU (in my understanding), it uses LAN and not the internet, and therefore, saves energy. Yup, [internet consumes a ton of energy!](https://www.forbes.com/sites/christopherhelman/2016/06/28/how-much-electricity-does-it-take-to-run-the-internet/))

# Connecting the two

If you've gone explored enough, you should know that Django itself has a server. At least for the time being, we will be using that.

So, firstly, start the server `python3 manage.py runserver`. Then, simply open the index.html in a browser. This should, at the least, work on your own computer. To make it work on other computers / virtual machines, we'd likely need to modify the address in axios-demo.js.

In addition, you may need to refer [this](https://stackoverflow.com/questions/43357687/django-python-rest-framework-no-access-control-allow-origin-header-is-present), if your browser gives an error, detected with the Developer Tools of your browser, on opening index.html.

[Learn markdown - Atlassian](https://confluence.atlassian.com/bitbucketserver/markdown-syntax-guide-776639995.html)


# Dependencies

Might be incomplete: django, django-cors-headers, curl, jq: (You may want to install the python modules in a system wide location by running the first two commands as sudo.)
    python3 -m pip install django
    python3 -m pip install django-cors-headers
    sudo apt install curl
    sudo apt install jq