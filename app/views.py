from django.shortcuts import render

# Create your views here.
def cdn_template(request):
    return render(request,'cdn_template.html')