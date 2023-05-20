from django.contrib import admin
from django.urls import path , include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

app_name="home"
urlpatterns = [
    path('manage/', admin.site.urls),
    path('', views.home, name="home"),
    path('work/',include('work.urls'), name="work"),
    path('about/',include('about.urls'), name="about"),
    path('connect/',views.connect,name="connect"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)