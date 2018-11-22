from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ('title', 'content', 'members', 'timeslot', 'published')
		