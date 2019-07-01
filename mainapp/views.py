from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse
from .models import Patient
from .forms import PatientAddForm,AddVisitDetailForm

# Create your views here.

def home(request):
    return render(request,"login.html")

def profile(request):
    count = Patient.objects.count()
    return render(request,"dashboard.html",{'count':count})

def addPatient(request):
    if request.method=="POST":
        form = PatientAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('searchpatient')+'?q='+form.cleaned_data['phone'])
        return render(request,'patient_add.html',{'form':form})
    return render(request, "patient_add.html",{"form":PatientAddForm()})

def searchpatient(request):
    q = request.GET.get('q',"")
    if len(q)==10: qs = Patient.objects.filter(phone=q)
    else:
        try:
            q = int(q)
            qs = Patient.objects.filter(pk=q)
        except: qs = Patient.objects.filter(name__iexact=q)
    return render(request,'searchpatient.html',{'qs':qs})

def addvisitdetail(request,pk):
    if request.method=="POST":
        patient = Patient.objects.get(pk=pk)
        form = AddVisitDetailForm(request.POST)
        if form.is_valid():
            v = form.save(commit=False)
            v.patient = patient
            v.save()
            return HttpResponseRedirect(reverse('visitdetail',args=[pk]))
        return render(request, "patient_add.html",{"form":form})
    return render(request, "patient_add.html",{"form":AddVisitDetailForm()})


def editpatient(request,pk):
    patient=Patient.objects.get(pk=pk)
    if request.method=="POST":
        form = PatientAddForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return HttpResponse("Edited successfully")
        else: return render(request,'patient_edit.html',{'form':form})
    form = PatientAddForm(instance=patient)
    return render(request,'patient_edit.html',{'form':form})

def visitdetails(request,pk):
    patient = Patient.objects.get(pk=pk)
    vd = patient.visitdetail_set.all().order_by('-pk')
    return render(request,'patientvisitdetail.html',{'patient':patient,'vd':vd})
