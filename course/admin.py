from django.contrib import admin
from course.models import Course, Category, Register, Event


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category')
    list_filter = ('category',)
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'site')
    list_filter = ('email',)
    search_fields = ('email',)


admin.site.register(Event)

