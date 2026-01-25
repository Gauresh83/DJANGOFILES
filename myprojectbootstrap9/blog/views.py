from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'blog/blog.html')
def base(request):
    return render(request,'base.html')


