from django.shortcuts import render
from django.contrib.auth.models import User


def instructor(request):
    teachers = User.objects.filter(role=0)
    context = {
        'teachers': teachers,
    }
    return render(request, 'instructors.html', context)

