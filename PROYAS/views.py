from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login , logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import Customer,Student
import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
import csv

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

def BASE(request):
    return render(request,'base.html')

def LOGIN(request):
    return render(request,'login.html')

def doLogin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request,
                                         username= request.POST.get('email'),
                                         password=request.POST.get('password'),)
        if user!= None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('admin_home')
            elif user_type == '2':
                return redirect('staff_home')
            else:
                messages.error(request,'Email and Password are Invalid !')
                return redirect('login')
        else:   
            messages.error(request,'Email and Password are Invalid !')     
            return redirect('login')
        
def doLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def PROFILE(request):
    user = Customer.objects.get(id=request.user.id)

    context ={
        "user" : user,
    }
    return render(request,'profile.html',context)


@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        # username = request.POST.get('username')
        password = request.POST.get('password')

    try:
        customuser = Customer.objects.get(id=request.user.id)

        customuser.first_name = first_name
        customuser.last_name = last_name
        
        if password !=None and password!= "":
                customuser.set_password(password)
        if profile_pic !=None and profile_pic!= "":
                customuser.profile_pic = profile_pic
        customuser.save()
        messages.success(request,'Your Profile Updated Successfully !')
        return redirect('profile')
    except:
        messages.error(request,'Failed to Update Your Profile !')

    return render(request,'profile.html')

def render_pdf_view(request,**kwargs):
    pk = kwargs.get('pk')
    
    try:
        student_details = get_object_or_404(Student,pk=pk)
        # result_card = Student.objects.get()
    except Student.DoesNotExist:
        messages.error(request, "Admit card not found.")
        return redirect( 'view_admit')

        # Render the template with the admit card details
    return render(request, 'Admit/admin_admit.html', {'student_details': student_details})

# def render_pdf_view(request,*args,**kwargs):
#     # student_details = Student.objects.all()
#     pk = kwargs.get('pk')
#     student_details = get_object_or_404(Student,pk=pk)
    
#     template_path = 'Admit/admin_admit.html'
#     context = {
#         'student_details': student_details,
#         }
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

#     response['Content-Disposition'] = ' filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#        html, dest=response)
#     # if error then show some funny view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response


#for landing page route
def landing_home(request):
    return render(request,'Landing_pages/homes.html')

def landing_about(request):
    return render(request,'Landing_pages/about.html')

def landing_downloads(request):
    return render(request,'Landing_pages/download.html')
def landing_notice(request):
    return render(request,'Landing_pages/notice.html')



def render_view_data(request, *args, **kwargs):
    pk = kwargs.get('pk')

    # districts_list = ['Alipurduar', 'Bankura', 'Birbhum', 'Cooch Behar', 'Dakshin Dinajpur',
    #                   'Darjeeling', 'Hooghly', 'Howrah', 'Jalpaiguri', 'Jhargram', 'Kalimpong',
    #                   'Kolkata', 'Malda', 'Murshidabad', 'Nadia', 'North 24 Parganas',
    #                   'Paschim Bardhaman', 'Paschim Medinipur', 'Purba Bardhaman',
    #                   'Purba Medinipur', 'Purulia', 'South 24 Parganas', 'Uttar Dinajpur']
    districts_list = [district for district, _ in DISTRICT_CHOICES]
    
    data_by_district = {}
    for district in districts_list:
        filtered_rows = Student.objects.filter(district=district)
        data_by_district[district] = filtered_rows

    # Assuming you want to generate a CSV file
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] =  filename="report.csv" 

    # Creating CSV writer
    writer = csv.writer(response)
    # Writing headers
    writer.writerow(['DISTRICT','CENTER CODE' ,'NAME' ,'GUARDIAN NAME','CLASSES','REG. NO','ROLL NO','SCHOOL NAME', 'MOBILE NUMBER'])
    # Writing data
    for district, students in data_by_district.items():
        for row in students:
            district_code = DISTRICT_CODE_MAP.get(district, '')
            # roll_no = district_code +"-" + str(row.center_codes) +  "-" + str(row.classes)  +"-"+ str(row.id)
            writer.writerow([district, row.center_codes , row.student_name, row.guardian_name ,row.classes  ,  f" {row.id}"  ,row.roll_no , row.school_name,  row.mobile_number])

    return response 


def RESULT(request):
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        student_name = request.POST.get('student_name')

        # Search for student by mobile number or name
        try:
            result_card = Student.objects.get(roll_no=roll_no, student_name=student_name)
        except Student.DoesNotExist:
            messages.error(request, "Admit card not found.")
            return redirect( 'result')

        # Render the template with the admit card details
        return render(request, 'Admit/result_card.html', {'reslut_card': result_card})
    
    return render(request, 'result.html')

def search_admit_card(request):
    if request.method == 'POST':
        mobile_number = request.POST.get('mobile_number')
        student_name = request.POST.get('student_name')

        # Search for student by mobile number or name
        try:
            admit_card = Student.objects.get(mobile_number=mobile_number, student_name=student_name)
        except Student.DoesNotExist:
            messages.error(request, "Admit card not found.")
            return redirect( 'admit')

        # Render the template with the admit card details
        return render(request, 'Admit/admit_card.html', {'admit_card': admit_card})
    
    return render(request, 'search.html')