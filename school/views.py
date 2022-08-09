from distutils.command import check
import imp
from multiprocessing import context
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages
from authapp.models import *
from teacher.models import *


from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
 
def assign_teacher(request):
    if request.method == 'POST':
            email = request.POST['t_email']
            name = request.POST['t_name']
            session = request.POST['session']
            subjects = request.POST['subjects']
            print("subjects------------=-=------------",subjects)
            form =AssignCourseTeacher(request.POST)
            print("------assign teacher")
            print(form.errors.as_data())
            if form.is_valid():
                print("------form valid teacher")
                assign_form=form.save(commit =False)
                teacher=Teacher.objects.get(t_info__email=email)
                school=School.objects.get(s_info__email=request.user)
                
                get_subject_detail=class_subject.objects.get(subject_class=assign_form.course_class,subject_name=subjects,subject_school__s_info__email=request.user)
                checking=AssignedTeacher.objects.filter(course_class=assign_form.course_class,course_session=session,course_school=school)
                
                print("checking email",email)
                print(checking)
                if not checking.exists():
                    assign_form.course_name=get_subject_detail
                    assign_form.course_teacher=teacher
                    assign_form.course_school=school
                    assign_form.course_session=session

                    assign_form.save()
                    return redirect('school_home')
                else:
                    form=AssignCourseTeacher()
                    messages.error(request,"class already assigned")

                    teachers=Teacher.objects.filter(t_school__s_info__email=request.user)
                    sessions=SchoolSessions.objects.all()
                    for i in teachers:
                        print(i.t_name)
                        print(i.t_info.email)
                    return render(request,'assign_teacher.html', {'form':form,'teachers':teachers,'sessions':sessions})
    form=AssignCourseTeacher()
    teachers=Teacher.objects.filter(t_school__s_info__email=request.user)
    sessions=SchoolSessions.objects.all()
    for i in teachers:
        print(i.t_name)
        print(i.t_info.email)
    return render(request,'assign_teacher.html', {'form':form,'teachers':teachers,'sessions':sessions})


   
def teacher_view(request):
    teachers=Teacher.objects.filter(t_school__s_info__email=request.user)
    for i in teachers:
        print("------------Teachers_name")
        print(i.t_name)
    context={
        'teachers':teachers,
    }
    return render(request,'teacher_view.html',context)

def teacher_delete(request,id):
    teacher_id=id
    obj = get_object_or_404(CustomUser, id = teacher_id)
    obj.delete()
    messages.error(request,"Teacher Deleted")
    return redirect('teacher_view')

def select_student(request):
    classes=AssignedTeacher.objects.filter(course_teacher__t_info__email=request.user)
    teacher_classes=[]
    teacher_session=[]
    for i in classes:
        print(i.course_class)
        print(i.course_session)
        teacher_classes.append(i.course_class)
        teacher_session.append(i.course_session)
    form=AddStudentForm()
    class_filter=set(teacher_classes)
    session_filter=set(teacher_session)
    teacher_classes=[]
    teacher_session=[]
    teacher_classes=list(class_filter)
    teacher_session=list(session_filter)
    context={
    'teacher_classes':teacher_classes,
    'teacher_session':teacher_session}
    return render(request,'teacher/select_student.html',context)


def add_marks(request):
    if request.method == 'GET':
 
        student_class=request.GET.get('student_class')
        
        student_roll=request.GET.get('student_roll')
        student_session=request.GET.get('student_session')
        print(student_session)
        if student_roll is not None:
            student_info1=Student.objects.get(student_roll=student_roll,student_class=student_class,student_session=student_session,student_teacher__t_info__username=request.user)

        form =AddMarks(request.GET)
        if form.is_valid() and student_roll is not None:
            student_marks=form.save(commit =False)
            print("-----------------English",student_marks.eng)
            student_marks.student_info=student_info1
            student_marks.save()
            print("")
        result=Student.objects.filter(student_teacher__t_info__email=request.user,student_class=student_class,student_session=student_session)
        for i in range(1):
            print(i)

        form=AddMarks()
        context={
            'student_class':student_class,
            'student_session':student_session,
            'form':form,
            'result':result
        }
        
        return render(request,'teacher/add_marks.html',context)


def submit_marks(request):
    if request.method == 'POST':

         form =AddMarks(request.POST)
         if form.is_valid():
            student_marks=form.save(commit =False)
            print(student_marks.eng)
 
            return redirect('add_marks')



def assign_subject(request):
    if request.method=='POST':
        form=AssignClassCourse(request.POST)
        if form.is_valid():
            print("subject is fine")
            subject=form.save(commit=False)
            school=School.objects.get(s_info__email=request.user)
            subject.subject_school=school
            subject.save()
            return redirect('school_home')

    form=AssignClassCourse()
    context={
        'form':form
    }
    return render(request,'school/assign_subject.html',context)

from django.db.models import Count

def view_subjects(request):
    filter_subject=class_subject.objects.filter(subject_school__s_info__email=request.user)
    print(filter_subject)
    dic={}
    value=0
    for i in filter_subject:
        if i.subject_class in dic:
            dic[i.subject_class]+=value
        else:      
            value=1 
            dic[i.subject_class]=value

    sort_data =sorted(dic.items(), key=lambda x: x[1])
    sort_data_dict = dict(sort_data)

    print(dic)
    context1={
        'dic':sort_data_dict
    }
    return render(request,'school/view_class_subjects.html',context1)


def view_class_subjects(request,key):
    class_subject1=key
    filter_subject=class_subject.objects.filter(subject_school__s_info__email=request.user,subject_class=class_subject1)
    context={
        'data':filter_subject,
        'class_no':class_subject1
    }
    return render(request,'school/view_specific_class.html',context)


    
def subject_delete(request,id):
    obj = get_object_or_404(class_subject, id = id)
    obj.delete()
    return redirect('school_home')



from django.http import JsonResponse

def get_topics_ajax(request):
    if request.method == "POST":
        print("Hey I am in ajax function")
        subject_class=request.POST.get('data')
        print(subject_class)
        try:
            subject = class_subject.objects.filter(subject_class = subject_class,subject_school__s_info__email=request.user)
        except Exception:
            print("Error in Ajax")
        return JsonResponse(list(subject.values('subject_name')), safe = False) 


def view_assigned_teachers(request):
        subjects=AssignedTeacher.objects.filter(course_school__s_info__email=request.user)
        for i in subjects:
            print(i.course_name.subject_name)

            print(i.course_name.subject_learning)
        context={
            'subjects': subjects
        }    
        return render(request,'school/view_assigned_teachers.html',context)
    
