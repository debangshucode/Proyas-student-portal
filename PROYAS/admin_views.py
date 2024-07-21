from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import  Customer ,Student ,Co_Ordinator
from django.contrib import messages

DISTRICT_CHOICES = (
    ('Alipurduar', '664'),
    ('Bankura', '305'),
    ('Birbhum', '307'),
    ('Cooch Behar', '308'),
    ('Dakshin Dinajpur', '310'),
    ('Darjeeling', '309'),
    ('Hooghly', '312'),
    ('Howrah', '313'),
    ('Jalpaiguri', '314'),
    ('Jhargram', '703'),
    ('Kalimpong', '702'),
    ('Kolkata', '315'),
    ('Malda', '316'),
    ('Murshidabad', '319'),
    ('Nadia', '320'),
    ('North 24 Parganas', '303'),
    ('Paschim Bardhaman', '704'),
    ('Paschim Medinipur', '318'),
    ('Purba Bardhaman', '306'),
    ('Purba Medinipur', '317'),
    ('Purulia', '321'),
    ('South 24 Parganas', '304'),
    ('Uttar Dinajpur', '311'),
)
    # Create a dictionary to map district names to codes
DISTRICT_CODE_MAP = dict(DISTRICT_CHOICES)
@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    co_ordinator_count = Co_Ordinator.objects.all().count()
    # student_gender_male = Student.objects.filter(gender='Male').count()
    # student_gender_male = Student.objects.filter(gender = 'Female').count()

    context = {
        'student_count':student_count,
        'co_ordinator_count':co_ordinator_count,
    }
    return render(request, 'Admin/home.html',context)

@login_required(login_url='/')
def ADD_STUDENT(request):
    # exam_name = ExamName.objects.all()
    # exam_session = ExamSession.objects.all()
    # district = Student.objects.all()
    districts = ['Alipurduar', 'Bankura', 'Birbhum', 'Cooch Behar', 'Dakshin Dinajpur',
                      'Darjeeling', 'Hooghly', 'Howrah', 'Jalpaiguri', 'Jhargram', 'Kalimpong',
                       'Kolkata', 'Malda', 'Murshidabad', 'Nadia', 'North 24 Parganas',
                       'Paschim Bardhaman', 'Paschim Medinipur', 'Purba Bardhaman',
                       'Purba Medinipur', 'Purulia', 'South 24 Parganas', 'Uttar Dinajpur']
                                                          
    if request.method == "POST":
        district = request.POST.get('district')
        center_codes = request.POST.get('center_codes')
        student_name = request.POST.get('student_name')
        guardian_name = request.POST.get('guardian_name')
        school_name = request.POST.get('school_name')
        classes = request.POST.get('classes')
        mobile_number = request.POST.get('mobile_number')
        
        district_code = DISTRICT_CODE_MAP.get(district, '')
        existing_count = Student.objects.filter(district=district, center_codes=center_codes, classes=classes).count()
        roll_no = f"{district_code}-{center_codes}-{classes}-{existing_count + 1}"

        student = Student( 
            district = district,
            center_codes = center_codes, 
            student_name = student_name,
            guardian_name = guardian_name,
            school_name = school_name ,
            classes = classes,
            mobile_number = mobile_number ,
            roll_no = roll_no,
        )
        student.save()
       
        messages.success(request,student.student_name + " successfully saved !")
        return redirect("addstudent")


    context = {
        'districts' : districts,

    }
    return render(request,'Admin/add_student.html',context)

def VIEW_STUDENT(request):
    student = Student.objects.all()

    


    context = {
        'student' : student,
        
    }
    return render(request,'Admin/view_student.html',context)

def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id=id)
    # exam_name = ExamName.objects.all()
    # exam_session = ExamSession.objects.all()


    context = {
        'student':student,
    }
    return render (request,'Admin/edit_student.html',context)


def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        district = request.POST.get('district')
        center_codes = request.POST.get('center_codes')
        student_name = request.POST.get('student_name')
        guardian_name = request.POST.get('guardian_name')
        school_name = request.POST.get('school_name')
        classes = request.POST.get('classes')
        mobile_number = request.POST.get('mobile_number') 
        roll_no = request.POST.get('roll_no')
        
        student = Student.objects.get(id=student_id)
        student.district = district
        student.center_codes = center_codes
        student.student_name = student_name
        student.guardian_name = guardian_name
        student.school_name = school_name
        student.classes = classes
        student.mobile_number = mobile_number
        student.roll_no = roll_no
        
        student.save()
        return redirect('view_student')

        
    return render(request,'Admin/edit_student.html')

def DOWNLOAD_STUDENT(request):
    districts = [
        'Alipurduar', 'Bankura', 'Birbhum', 'Cooch Behar', 'Dakshin Dinajpur',
        'Darjeeling', 'Hooghly', 'Howrah', 'Jalpaiguri', 'Jhargram', 'Kalimpong',
        'Kolkata', 'Malda', 'Murshidabad', 'Nadia', 'North 24 Parganas',
        'Paschim Bardhaman', 'Paschim Medinipur', 'Purba Bardhaman',
        'Purba Medinipur', 'Purulia', 'South 24 Parganas', 'Uttar Dinajpur'
    ]
    context = {
        # 'student' : student,
        'districts':districts,
        
    }
    return render(request,"Admin/download_student.html",context)



def ADD_STAFF(request):
    districts = [
        'Alipurduar', 'Bankura', 'Birbhum', 'Cooch Behar', 'Dakshin Dinajpur',
        'Darjeeling', 'Hooghly', 'Howrah', 'Jalpaiguri', 'Jhargram', 'Kalimpong',
        'Kolkata', 'Malda', 'Murshidabad', 'Nadia', 'North 24 Parganas',
        'Paschim Bardhaman', 'Paschim Medinipur', 'Purba Bardhaman',
        'Purba Medinipur', 'Purulia', 'South 24 Parganas', 'Uttar Dinajpur'
    ]
    context={
        'districts':districts,
    }

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        district = request.POST.get('district')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if Customer.objects.filter(email=email).exists():
            messages.warning(request,"Email already exists !")
            return redirect('coordinator')
        if Customer.objects.filter(username=username).exists():
            messages.warning(request,"Username already exists !")
            return redirect('coordinator')
        else:
            user = Customer(
                first_name = first_name,
                last_name = last_name ,
                email = email ,
                username = username,
                user_type = 2
            )
            user.set_password(password)
            user.save()
            staff = Co_Ordinator(
                admin = user,
                district = district ,
            )
            staff.save()
            messages.success(request," Co Ordinator Successfully Added !")
            return redirect('coordinator')

    return render(request,'Admin/add_ordinator.html',context)

def DJANGO_ADMIN(request):
    pass

