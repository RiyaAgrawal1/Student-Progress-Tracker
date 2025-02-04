from ast import Assign
from msilib.schema import Class
from statistics import mode
from django.db import models
from django.conf import settings

from authapp.models import GovtSubject

# Create your models here.

COURSE_CHOICES= [
        ('English', 'English'),
        ('Maths', 'Maths'),
        ('Science', 'Science'),
        ('Hindi', 'Hindi'),
        ('Marathi', 'Marathi'),
        ('History', 'History'),
        ('Geography', 'Geography'),
        ('Sanskrit', 'Sanskrit'),
 
        ]
CLASS_CHOICES= [
        ('1', 'Standard 1'),
        ('2', 'Standard 2'),
        ('3', 'Standard 3'),
        ('4', 'Standard 4'),
        ('5', 'Standard 5'),
        ('6', 'Standard 6'),
        ('7', 'Standard 7'),

        ]
class School(models.Model):
    s_name =models.CharField(max_length =255, null=True,blank=True)
    s_district =models.CharField(max_length =255, null=True,blank=True)
    s_city =models.CharField(max_length =255, null=True,blank=True)
    s_info= models.ForeignKey(settings.AUTH_USER_MODEL,db_index=True,on_delete =models.CASCADE)
    

    def __str__(self):
        return self.s_name

class Teacher(models.Model):
    t_name=models.CharField(max_length =255, null=True,blank=True)
    t_school =models.ForeignKey( School,on_delete=models.CASCADE)
    t_info= models.ForeignKey(settings.AUTH_USER_MODEL,db_index=True,on_delete =models.CASCADE)
    def __str__(self):
        return self.t_name

'''
class Classes(models.Model):
    c_standard=models.CharField(max_length =255, null=True,blank=True)
    c_school =models.ForeignKey( School,related_name='school_info',on_delete=models.CASCADE)
    c_teacher =models.ForeignKey( Teacher,related_name='teacher_info',on_delete=models.CASCADE)
'''

class SchoolSessions(models.Model):
    session=models.CharField(max_length =255,null=True,blank=True)
    def __str__(self):
        return self.session


class school_class_subject(models.Model):
    subject_info=models.ForeignKey( GovtSubject, on_delete=models.CASCADE, null=True,blank=True)
    subject_school=models.ForeignKey( School, on_delete=models.CASCADE, null=True,blank=True,)

    def __str__(self):
        return self.subject_school.s_name


class SchoolAssignedTeacher(models.Model):
    course_name=models.ForeignKey( school_class_subject, on_delete=models.CASCADE)
    course_teacher=models.ForeignKey( Teacher, on_delete=models.CASCADE)
    course_school=models.ForeignKey( School, on_delete=models.CASCADE)
    course_session=models.CharField(max_length =255,null=True,blank=True)
    def __str__(self):
        return self.course_session


class class_subject(models.Model):
    subject_name=models.CharField(max_length =255, null=True,blank=True,choices=COURSE_CHOICES)
    subject_class=models.CharField(max_length =255, null=True,blank=True,choices=CLASS_CHOICES)
    subject_learning=models.IntegerField(null=True,blank=True,default=0)
    subject_school=models.ForeignKey( School, on_delete=models.CASCADE)
    subject_copdf=models.FileField(upload_to='COpdf/', blank=True, null=True)
    def __str__(self):
        return self.subject_school.s_name


class AssignedTeacher(models.Model):
    course_name=models.ForeignKey( class_subject, on_delete=models.CASCADE)
    course_class=models.CharField(max_length =255,null=True,blank=True,choices=CLASS_CHOICES)
    course_teacher=models.ForeignKey( Teacher, on_delete=models.CASCADE)
    course_school=models.ForeignKey( School, on_delete=models.CASCADE)
    course_session=models.CharField(max_length =255,null=True,blank=True)
    def __str__(self):
 
        return self.course_class


        
class Student(models.Model):
    student_roll=models.IntegerField( null=True,blank=True)
    student_name=models.CharField(max_length =255, null=True,blank=True)
    #
    #student_course_name=models.CharField(max_length =255, null=True,blank=True)
    student_school =models.ForeignKey( School, on_delete=models.CASCADE)
    student_teacher =models.ForeignKey( Teacher, on_delete=models.CASCADE)
    student_class=models.CharField(max_length =255, null=True,blank=True)
    student_session=models.CharField(max_length =255,null=True,blank=True)
    def __str__(self):
        return self.student_school.s_name+"___"+self.student_name

 






class StudentMarks(models.Model):
    student_info=models.ForeignKey( Student, on_delete=models.CASCADE)
    eng=models.IntegerField(null=True,blank=True,default=0)
    math=models.IntegerField(null=True,blank=True,default=0)
    sci=models.IntegerField(null=True,blank=True,default=0)
    sst=models.IntegerField(null=True,blank=True,default=0)
    hindi=models.IntegerField(null=True,blank=True,default=0)
    tot=models.IntegerField(null=True,blank=True,default=0)
    per=models.FloatField(null=True,blank=True,default=0)
    def __str__(self):
        return self.student_info.student_name


class AssignSportTeacher(models.Model):
    sport_class=models.CharField(max_length =255,null=True,blank=True,choices=CLASS_CHOICES)
    sport_teacher=models.ForeignKey( Teacher, on_delete=models.CASCADE)
    sport_school=models.ForeignKey( School, on_delete=models.CASCADE)
    sport_session=models.CharField(max_length =255,null=True,blank=True)
    def __str__(self):
        return self.sport_class


class AssignCulturalTeacher(models.Model):
    cul_class=models.CharField(max_length =255,null=True,blank=True,choices=CLASS_CHOICES)
    cul_teacher=models.ForeignKey( Teacher, on_delete=models.CASCADE)
    cul_school=models.ForeignKey( School, on_delete=models.CASCADE)
    cul_session=models.CharField(max_length =255,null=True,blank=True)
    def __str__(self):
        return self.cul_class




class StudentAccount(models.Model):
    student_info=models.ForeignKey( Student,on_delete=models.CASCADE)
    s_school =models.ForeignKey( School,on_delete=models.CASCADE)
    s_info= models.ForeignKey(settings.AUTH_USER_MODEL,db_index=True,on_delete =models.CASCADE)
    def __str__(self):
        return self.s_info.email

class COINFO(models.Model):
    co_no=models.CharField(max_length =255,null=True,blank=True)
    co_info=models.CharField(max_length =255,null=True,blank=True)
    co_teacher=models.ForeignKey( Teacher, on_delete=models.CASCADE)
    co_school=models.ForeignKey( School, on_delete=models.CASCADE)
    co_class=models.CharField(max_length =255,null=True,blank=True)