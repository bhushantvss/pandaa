from django.contrib import admin
from django.urls import path
from App1.views import Get_Practice_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', Get_Practice_data.as_view(), name='get_data')
]
