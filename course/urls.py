from django.urls import path
from course.views import index, login_view, course_view, detail, regular


urlpatterns = [
    path('', index, name='index'),
    path('login_view/', login_view, name='login_view'),
    path('course_view/', course_view, name='course_view'),
    path('regular/', regular, name='regular'),
    path('course_detail/<int:pk>/', detail, name='course_detail'),
]