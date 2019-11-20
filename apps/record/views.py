from django.shortcuts import render, redirect
from .forms import RecordForm
from .models import Record

def Home(request):
    return render(request, 'index.html')

def createRecord(request):
    if request.method == 'POST':
        print(request.POST)
        record_form = RecordForm(request.POST)
        if record_form.is_valid():
            record_form.save()
            return redirect('index')
    else:
        record_form = RecordForm()
        print(record_form)
    return render(request, 'record/create_data.html',{'record_form_view': record_form})

def showRecord(request):
    records = Record.objects.all()
    return render(request, "record/data_sensor.html", {"list_autores": records})