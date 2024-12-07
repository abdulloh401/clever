from django.shortcuts import render, get_object_or_404
from course.models import Course, Event, Category
from course.forms import RegisterForm
from blog.models import Blog
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    events = Event.objects.all()[:3]
    course = Course.objects.all()[:6]
    blog = Blog.objects.all()[:4]
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
    categories = Category.objects.order_by('?')[:1]
    context = {
        'course': course,
        'events': events,
        'form': form,
        'blog': blog,
        'categories': categories,
    }
    return render(request, 'index.html', context)


@login_required(login_url='login')
def login_view(request):
    return render(request, 'index-login.html')


@login_required(login_url='login')
def course_view(request):
    page = request.GET.get('page')
    paginator = Paginator(Course.objects.all(), 6)
    courses = paginator.get_page(page)
    if not page:
        page = 1
    context = {
        'page': page,
        'courses': courses,
    }
    return render(request, 'courses.html', context)


@login_required(login_url='login')
def detail(request, pk):
    course = get_object_or_404(Course.objects.all(), id=pk)
    three_course = Course.objects.order_by('?')[:3]
    category = course.category
    teachers = User.objects.filter(role=0)
    context = {
        'course': course,
        'teachers': teachers,
        'three_course': three_course,
    }
    return render(request, 'single-course.html', context)


@login_required(login_url='login')
def regular(request):
    return render(request, 'regular-page.html')
