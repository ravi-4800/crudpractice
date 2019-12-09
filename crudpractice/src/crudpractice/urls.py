"""crudpractice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from employee.views import emp_create_view, emp_details_view, emp_update_view, emp_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', emp_create_view),
    path('emp_details/', emp_details_view),
    path('emp_details/delete/<int:emp_id>',emp_delete_view),
    path('emp_details/update/<int:emp_id>',emp_update_view)


]
