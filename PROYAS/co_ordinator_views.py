from django.shortcuts import render,redirect
from app.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def HOME(request):
    return render (request,'co_ordinator/home.html')

@login_required(login_url='/')
def ADD_STUDENT(request):
    districts = [
        'Alipurduar', 'Bankura', 'Birbhum', 'Cooch Behar', 'Dakshin Dinajpur',
        'Darjeeling', 'Hooghly', 'Howrah', 'Jalpaiguri', 'Jhargram', 'Kalimpong',
        'Kolkata', 'Malda', 'Murshidabad', 'Nadia', 'North 24 Parganas',
        'Paschim Bardhaman', 'Paschim Medinipur', 'Purba Bardhaman',
        'Purba Medinipur', 'Purulia', 'South 24 Parganas', 'Uttar Dinajpur'
    ]
    if request.method == "POST":
        district = request.POST.get('district')
        center_codes = request.POST.get('center_codes')
        student_name = request.POST.get('student_name')
        guardian_name = request.POST.get('guardian_name')
        school_name = request.POST.get('school_name')
        classes = request.POST.get('classes')
        mobile_number = request.POST.get('mobile_number')
        

        student = Student( 
            district = district,
            center_codes = center_codes, 
            student_name = student_name,
            guardian_name = guardian_name,
            school_name = school_name ,
            classes = classes,
            mobile_number = mobile_number , 
        )
        student.save()
       
        messages.success(request,student.student_name + " successfully saved !")
        return redirect("coaddstudent")
    return render(request,'co_ordinator/coadd_student.html',{'districts' : districts})

def VIEW_STUDENT(request):
    Alipurduar = Student.objects.filter(district='Alipurduar')
    Bankura = Student.objects.filter(district='Bankura')
    context={
        'Alipurduar':Alipurduar,
        'Bankura':Bankura,
    }
    # for row in filtered_rows_Alipurduar:
    #     print(row.district, row.center_codes, row.student_name, row.guardian_name, row.school_name, row.classes, row.mobile_number)
    # filtered_rows_Bankura = Student.objects.filter(district='Bankura')
    # for row in filtered_rows_Bankura:
    #     print(row.district, row.center_codes, row.student_name, row.guardian_name, row.school_name, row.classes, row.mobile_number)
    return render(request,"co_ordinator/coview_student.html",context)


