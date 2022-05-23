from django.http import HttpResponse
from django.shortcuts import render
from courses.models import Courses,Category,Roadmap
from home.forms import SearchForm

# Create your views here.
def index(request):
    coursesdata = Courses.objects.all().order_by('-id')[:1000]
    context={'coursesdata':coursesdata, 'page':'home'}
    return render(request, 'index.html', context)

def aboutus(request):
    context={'page':'aboutus'}
    return render(request, 'aboutus.html', context)

def course_detail(request,id):
    course=Courses.objects.get(pk=id)
    roadmap=Roadmap.objects.filter(course_id=id)
    context={'page':'course_detail',
             'course':course,
             'roadmap': roadmap}
    return render(request, 'course_detail.html', context)

def course_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            courses = Courses.objects.filter(title__icontains=query)
            context={'page':'search',
             'courses':courses}
            return render(request, 'search.html', context)
def categories(request):
    categoriesdata = Category.objects.all().order_by('title')[:1000]
    context={'categoriesdata':categoriesdata, 'page':'categories'}
    return render(request, 'categories.html', context)

def category_detail(request,id):
    courses=Courses.objects.filter(category_id=id)
    context={'page':'category_detail',
             'courses':courses}
    return render(request, 'category_detail.html', context)

# Create your views here.
#def index(request):
 #   text="Merhaba burası courses ana sayfası "
 #   return HttpResponse("%s." % text)