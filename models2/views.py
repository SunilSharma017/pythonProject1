from django.http import HttpResponse
from django.shortcuts import render,redirect
from data2.models import Student,OtherInformation
def Home(request):
    if request.method=="POST":
        name=request.POST.get("n1")
        father_name=request.POST.get("n2")
        mother_name=request.POST.get("n3")
        mobile=request.POST.get("num")
        dob=request.POST.get("n4")
        city=request.POST.get("n5")
        state=request.POST.get("n6")
        email=request.POST.get("n7")
        password=request.POST.get("n8")
        cpassword=request.POST.get("n9")
        gender=request.POST.get("n10")
        subjects=request.POST.getlist("n11")

        Student.objects.create(
            name=name,
            father_name=father_name,
            mother_name=mother_name,
            mobile=mobile,
            dob=dob)
        OtherInformation.objects.create(
            city=city,
            state=state,
            email=email,
            password=password,
            cpassword=cpassword,
            gender=gender,
            subjects=subjects,)
        
        dct={
             "name":name,
            "father_name":father_name,
            "mother_name":mother_name,
            "mobile":mobile,
            "dob":dob,
            "city":city,
            "state":state,
            "email":email,
            "password":password,
            "cpassword":cpassword,
            "gender":gender,
            "subjects":subjects,
        }
        return render(request,"success.html",dct)
    return render(request,"index.html")

