from django.shortcuts import render, get_object_or_404
from blog.models import Category, Blog, Comment
from django.core.paginator import Paginator
from blog.forms import CommentForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def blog(request):
    category = request.GET.get('category')
    page = request.GET.get('page')
    if category:
        paginator = Paginator(Blog.objects.filter(category__title=category), 4)
    else:
        paginator = Paginator(Blog.objects.all(), 4)
    blogs = paginator.get_page(page)
    categories = Category.objects.all()
    if not page:
        page = 1
    context = {
        'page': page,
        'paginator': paginator,
        'category': category,
        'categories': categories,
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)


@login_required(login_url='login')
def blog_detail(request, pk):
    blogs = get_object_or_404(Blog.objects.all(), id=pk)
    category = blogs.category
    blog_two = Blog.objects.filter(category=category).order_by('?')[:2]
    comments = Comment.objects.filter(blog=blogs)[:2]
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.blog = blogs
            form.save()
    context = {
        'blogs': blogs,
        'blog_two': blog_two,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog-details.html', context)

