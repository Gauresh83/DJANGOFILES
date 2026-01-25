from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    students_list = [
        {'name': 'Alice', 'age': 24},
        {'name': 'Bob', 'age': 22},
        {'name': 'Charlie', 'age': 23},
    ]
    return render(request,'blog/about.html',{'students':students_list})

   