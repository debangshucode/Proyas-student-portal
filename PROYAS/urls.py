"""
URL configuration for PROYAS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, admin_views , co_ordinator_views  


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('base/',views.BASE,name='base'),

    #login
    path('login',views.LOGIN, name='login'),
    path('dologin', views.doLogin, name='doLogin'),
    path('dologout',views.doLogout, name='doLogout'),

    #profile update
    path('profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE, name='profile_update'),

    #this is admin panel
    path('Admin/Home',admin_views.HOME, name='admin_home'),
    path('Admin/Student/Add',admin_views.ADD_STUDENT,name="addstudent"),
    path('Admin/Student/view',admin_views.VIEW_STUDENT,name='view_student'),
    path('Admin/Student/edit/<str:id>',admin_views.EDIT_STUDENT, name='edit_student'),
    path('Admin/Student/update',admin_views.UPDATE_STUDENT, name = "update_student"),
    path('Admin/Student/download',admin_views.DOWNLOAD_STUDENT,name="download_student"),
    path('Admin/Student/viewdata',views.render_view_data,name="view_data"),
    path('Admin/Student/viewdata_Bankura',views.render_view_data,name="view_data_Bankura"),

    #Link for Co-Ordinator 
    path('Admin/Staff/add',admin_views.ADD_STAFF,name = 'coordinator'),
    path('Co_ordinator/Home',co_ordinator_views.HOME,name="staff_home"),
    path('Co_ordinator/Student/Add',co_ordinator_views.ADD_STUDENT,name="coaddstudent"),
    path('Co_ordinator/Student/view',co_ordinator_views.VIEW_STUDENT,name='coview_student'),

    
    #admit card generate
    path('Admit/admit_card/<pk>/',views.render_pdf_view,name='view_admit'),
    

    #landing page links
    path('',views.landing_home,name='landing_home'),
    path('Home/about',views.landing_about,name='landing_about'),
    path('Home/downloads',views.landing_downloads,name='landing_downloads'),
    path('Home/notice',views.landing_notice,name="landing_notice"),

    #result 
    # path('Home/result',views.RESULT,name="result"),
    path('Home/admit',views.search_admit_card,name="admit"),

    #admin panel
    path('admin/app/student/',admin_views.DJANGO_ADMIN,name="django_admin"),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
