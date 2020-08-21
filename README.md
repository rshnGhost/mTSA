## mTSA
A simple django project which should be exended to future website as needed.

## Requirements
Chocolatey (One click Install file avaliable) [installChocolatey.bat]
Python 3.8.5 (One click Install file avaliable) [1 install.bat]

## Installation (Windows)
# Install Chocolatey (should have internet connection) (skip if Installed)
Double click on "installChocolatey.bat"

# Install Python using Chocolatey (should have internet connection)
Right click on "1 install.bat" and run as Administrator

# Setup the Project
Double click on "2 setup.bat"

Fill all credentials in the Notepad that pops up.

Give the details for superuser to be created.

## Usage (Windows)
Double click on "3 run.bat"

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
