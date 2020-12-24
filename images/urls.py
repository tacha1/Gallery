from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome, name = 'welcome'),
    url(r'^search/', views.search_image, name='search_image'),
    url(r'^image/(\d+)', views.image, name='image'),
    url(r'^location/(\d+)', views.image_location, name = 'location'),
    url(r'^copy/(\d+)', views.copy_image_url, name = 'copy'),
] 

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
