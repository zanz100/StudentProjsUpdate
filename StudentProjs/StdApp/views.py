from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from .models import Contact

# Create your views here.
def index(request):
    if request.method=="POST":
        usn = request.POST.get('usn','')
        name = request.POST.get('name','')
        sem = request.POST.get('sem','')
        mobile_no = request.POST.get('mobile_no','')
        email = request.POST.get('email','')
        if usn and name and sem and mobile_no and email:
            contact=Contact(usn=usn,name=name,sem=sem,mobile_no=mobile_no,email=email)
            contact.save()
        else:
            return  HttpResponse("Pls input correct details")
    return render(request, 'index.html')