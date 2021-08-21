
from django.contrib import admin
from django.urls import path
from emailapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.email_view,name='email_view'),
]

