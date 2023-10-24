from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.contrib import messages


#this function will add new item and show all item
def add_show(request):
    """
    The function "add_show" is used to handle a POST request to add a new student registration form and
    display all existing student registrations.
    
    :param request: The request object represents the HTTP request that the server receives from the
    client. It contains information such as the HTTP method (GET, POST, etc.), headers, and any data
    sent in the request
    :return: a rendered HTML template called 'addandshow.html' along with a context dictionary
    containing the form object 'fm' and the queryset 'stud'.
    """
    
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        
        if fm.is_valid():
            fm.save()
            HttpResponseRedirect('/')
    else:
    
        fm = StudentRegistration()
        
    stud = User.objects.all()
    
    return render(request, 'enroll/addandshow.html', {'form' : fm, 'stu': stud})

#this function will data item from database
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        
        messages.success(request, "Record deleted successfully!")
        return HttpResponseRedirect('/')
    
#this function will update/edit
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        messages.success(request, "Record updated successfully!")
    
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        
    return render(request, 'enroll/updatestudent.html', {"form": fm})