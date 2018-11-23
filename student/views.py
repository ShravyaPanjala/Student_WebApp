# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import StudentProfile
from .forms import StudentForm
# Create your views here.
def homeview(request):
	form=StudentForm()
	msg=""
	if request.method=="POST":
		student_profile=StudentForm(request.POST)
		if student_profile.is_valid():
			StudentProfile.objects.create_user(**student_profile.cleaned_data)
			msg="success"
		else:
			msg=student_profile._errors

	return render(request,"student_profile.html",{"form":form,"msg":msg})

def students_view(request):
	data=StudentProfile.objects.all()
	return render(request,"students_data.html",{"objects":data})
