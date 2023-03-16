from django.shortcuts import render,redirect
from . models import Task
from . forms import TodoForm
from django.views.generic import ListView # ListView is a inbuilt class
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

class TaskListView(ListView):
    model = Task  # here we mention our table name
    template_name = 'home.html'  #mention name of the template should be display
    context_object_name = "task1"  # mention the key of variable name where all the objects of db saved

class TaskDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'
    
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority','date')
    
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
    
        

# Create your views here.
def add(request):
    
    if request.method == 'POST':   # coz in form we r using the method post 
        name1 = request.POST.get('task','')  # to get the task name from the user
        priority1 = request.POST.get('priority','')  #  to get the priority from the user
        date1 = request.POST.get('date','')
        task = Task(name = name1, priority = priority1,date=date1)   # to add the name,priority to the respect column in the table task
        task.save()  #to save the details the database permenently
        
    task1 = Task.objects.all()  # to fetch all the data stored in the table (Task) from the database
    return render(request,'home.html',{'task1':task1}) #to show or display the HTML homepage


def delete(request,taskid):
    task = Task.objects.get(id = taskid) # we are getting all the taskid 
    if request.method == 'POST':
        task.delete() # this inbuilt function wil delete 
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task = Task.objects.get(id = id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})





