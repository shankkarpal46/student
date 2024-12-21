from django.shortcuts import render,HttpResponseRedirect
from django.views import View
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class User_Login(View):
    def get(self,request):       
        return render(request,"login.html")
    
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            print(request.user.first_name)
            return HttpResponseRedirect("/display-student")
        else:
            return render(request,"login.html",{'message':'Login Failed.'})
        
class User_Logout(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect("/login")
    
def student(request):
    if request.method == 'GET':
        return render(request,"student_form.html",{})
    
    if request.method == 'POST':
        return HttpResponseRedirect('user/display-student')
    
class User_Register(View):
    def get(self,request):
        form = CustomUserCreationForm()
        return render(request,"register.html",{"form":form})

    def post(self,request):
        submitted_form = CustomUserCreationForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
            return HttpResponseRedirect("/login")
        return render(request,"register.html",{"form":submitted_form})
    
class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = "/display-student"
    template_name = "student/student_register.html"

class Student_ListView(ListView):
    model = Student 
    template_name = "student/student_list.html"
    context_object_name="object_list"

class Student_UpdateView(UpdateView):
    model = Student
    fields = ['student_image','student_first_name','student_middle_name','student_last_name','student_date_birth','student_address','student_email','student_contact_number','student_course']
    success_url = '/display-student'
    template_name = 'student/student_register.html'

class DeleteView(DeleteView):
    model = Student
    success_url = "/display-student"
    template_name = 'student/delete_student.html'
