from django import forms
from models import StudentProfile
class StudentForm(forms.ModelForm):
	class Meta:
		model=StudentProfile
		fields=["username","age","gender"]