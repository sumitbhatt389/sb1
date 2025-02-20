from django.shortcuts import render
# Create your views here.
def learn_django(request):
    coursename = {'cname' : 'React'}
    return render(request, 'course/courseone.html',
context=coursename                  )




def learn_python(request):
    return render(request, 'course/coursetwo.html')