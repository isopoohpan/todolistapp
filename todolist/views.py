from django.shortcuts import render
from .models import Todo
from .models import Member
from .forms import TodoForm
from django.utils import timezone
from django.shortcuts import *
# Create your views here.


def list(request):
	if 'ajax' in request.GET:
		search_str = request.POST['search']
		print(search_str)
		tasks = Todo.objects.filter(title__icontains=search_str)
		print(tasks)
		return render(request, 'ajaxlist.html', {'tasks': tasks})
	tasks = Todo.objects.all()
	return render(request, 'list.html', {'tasks':tasks})

def add(request):
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.created_date = timezone.now()
			todo.save()
			return redirect('list')
	else:
		form = TodoForm()
	return render(request, 'add.html', {'form': form});

def edit(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	print(todo)
	if request.method == "POST":
		form = TodoForm(request.POST, instance=todo)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.save()
			return redirect('list')
	else:
		form = TodoForm(instance=todo)
	return render(request, 'edit.html', {'form': form})

def delete(request, pk):
	todo = Todo.objects.get(pk=pk)
	todo.delete()
	return redirect('list')

