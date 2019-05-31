from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # use urls.py from articles directory for localhost:8000/articles prefix
    url(r'^articles/', include("articles.urls")),
]
