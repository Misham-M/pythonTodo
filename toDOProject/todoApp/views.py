from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import Todoform

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django .views.generic.edit import UpdateView,DeleteView

# class based

class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'allTask'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'Task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update2.html'
    context_object_name = 'Task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy("cbvdetail",kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete2.html'
    success_url = reverse_lazy('cbvindex')
# Create your views here.
def index(request):
    allTask = Task.objects.all()
    if request.method == 'POST':
        name=request.POST.get("name","")
        priority=request.POST.get("priority","")
        date=request.POST.get("date","")
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,"index.html",{'allTask':allTask})
def details(request):
    allTask=Task.objects.all()
    return render(request,"details.html",{'allTask':allTask})
def delete(request,taskId):

    # task=request.POST.get(id=taskId)
    task=Task.objects.get(id=taskId)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    f=Todoform(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'f':f,'task':task})