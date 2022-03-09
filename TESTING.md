# Testing

A variety of manual and automated tests were performed throughout the project.

## Manual Testing

#1. Getting the live deployed site working. This is well documented in the latter sections of [DEPLOYMENT.md](DEPLOYMENT.md)

#2. Checking the deployed site opens on the homepage.
- created a function based view in home
- created a path in the url file in the home app
- referenced in the home app url and the main project url file

*home/views.py*
``` Python
def index(request):
    """
    Index view
    """
    return render(request, 'home/index.html')
```
*home/urls.py*
``` Python
path('', views.index, name='home'),
```
*main/urls.py*
``` Python
path('', include("home.urls")),
```

![live-deployment-homepage](docs/readme/testing/01-live-deployment-homepage.png "live-deployment-homepage")


## Automated Testing

Return to[README.md](README.md)