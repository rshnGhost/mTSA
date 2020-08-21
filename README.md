## mTSA
A simple django project which should be exended to future website as needed.

## Requirements
Python 3.7.2

## Installation (Windows)
Double click on install.bat (should have internet connection)

Fill all credentials in the Notepad that pops up.

Give the details for superuser to be created.

## Usage (Windows)
Double click on run.bat

open browser and goto http://127.0.0.1:8000

## Addons
Add your apps to the project and use them.

## register your apps
open src/settings.py in your editor.

under INSTALLED_APPS list add your app name with qoutes and ending with comma

example:
    INSTALLED_APPS = [
    
        ...
        
        'myapp',
        
        ...
        
    ]

open src/urls.py in your editor.

# import your app urls
from myapp import urls

# include your app urls
urlpatterns = [

...

url(r'^myapp/', include('myapp.urls')),

...

]

Enjoy :)
