from django import forms

from .models import Employee

class EmpDetailForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = [
			'name',
			'company_id',
			'age',
			'email',
			'location',
			'designation',
			'skill'
		]