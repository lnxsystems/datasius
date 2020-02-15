## Website APP

This is the code for the django website app. It takes care of various datasius
website functions such as 


### 
Directory layout

```
├── data
│   └── db.sqlite3
├── Dockerfile
├── Makefile
├── manage.py
├── README.md
├── requirements.txt
├── run.sh
└── website
    ├── asgi.py
    ├── __init__.py
    ├── __pycache__
    ├── settings.py
    ├── static
    ├── templates
    ├── urls.py
    ├── views.py
    └── wsgi.py
```

### Accounts and Registration

The following third party apps are used

* django-registration
* django.contrib.auth

#### URLS 

The django.contrib.auth provides /accounts urls as follows:

```
accounts/ activate/complete/ [name='django_registration_activation_complete']
accounts/ activate/<str:activation_key>/ [name='django_registration_activate']
accounts/ register/ [name='django_registration_register']
accounts/ register/complete/ [name='django_registration_complete']
accounts/ register/closed/ [name='django_registration_disallowed']
accounts/ login/ [name='login']
accounts/ logout/ [name='logout']
accounts/ password_change/ [name='password_change']
accounts/ password_change/done/ [name='password_change_done']
accounts/ password_reset/ [name='password_reset']
accounts/ password_reset/done/ [name='password_reset_done']
accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/ reset/done/ [name='password_reset_complete']
```
