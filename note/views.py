from django.shortcuts import render,redirect
from .models import todo
def home(request):
    data=todo.objects.all()
    return render(request,'home.html',{'data':data})
def add(request):
 text = request.POST['notes']
 textarea = todo(content = text)
 textarea.save()
 return redirect(home)
def delete(request ,to_id):
    item=todo.objects.get(id=to_id)
    item.delete()
    return redirect(home)

