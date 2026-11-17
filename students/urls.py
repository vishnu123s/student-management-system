from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_student),
    path('students/',views.student_list),
    path('delete/<int:id>/', views.delete_student),
    path('update/<int:id>/', views.update_student),
]