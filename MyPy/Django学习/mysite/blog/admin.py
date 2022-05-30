from django.conf.urls import url
from django.contrib import admin

from views import index

# Register your models here.
urlpatterns = [
    url(r'^admin/', admin.site.urls,
        url(r'^index/', index))
]
