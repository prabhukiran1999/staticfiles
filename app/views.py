from django.shortcuts import render

# Create your views here.
def styles(request):
    return render(request,'styles.html')