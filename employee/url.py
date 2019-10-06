from django.contrib import admin
from django.urls import path,include
from employee import views
urlpatterns = [
    path('add_emp/',views.add_emp),
    path('add_emp_msg/', views.add_emp_msg),
    path('emplist/', views.emplist),
    path('update_emp/', views.update_emp),
    path('update/', views.update),
    path('delete_emp/', views.delete_emp),
]