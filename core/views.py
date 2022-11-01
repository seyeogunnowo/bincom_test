from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *
import random

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def polling_units_results(request):
    if request.method=='POST':
         return render(request, 'core/polling_units_results.html', {
        'all_pu':PollingUnit.objects.all(),
        'pu_results':AnnouncedPuResults.objects.all(),
        'selected_pu_id':request.POST['polling_unit']

    })
    return render(request, 'core/polling_units_results.html', {
        'all_pu':PollingUnit.objects.all(),
    })

def lga_sum_results(request):
    if request.method=='POST':
        apr_data=[]
        for pu in PollingUnit.objects.all():
          if pu.lga_id == request.POST['lga']:
            for apr in AnnouncedPuResults.objects.all():
                if apr.polling_unit_uniqueid == pu.uniqueid:
                    apr_data.append(apr)   
        return render(request, 'core/lga_sum_results.html', {
        'all_lga':Lga.objects.all(),
        'apr_data':apr_data,
        'pu_list': PollingUnit.objects.filter(lga_id=int(request.POST['lga']))

    })
    return render(request, 'core/lga_sum_results.html', {
        'all_lga':Lga.objects.all(),
    })

def create_polling_unit(request):
    if request.method=='POST':
        randomly_generated_unique_id=random.randint(1000, 10000)
        PollingUnit.objects.create(uniqueid=randomly_generated_unique_id,polling_unit_name=request.POST['name'], polling_unit_description=request.POST['description'], lat=request.POST['latitude'], long=request.POST['longitude'], ward_id=request.POST['ward'], lga_id=request.POST['lga'])
        AnnouncedPuResults.objects.create(polling_unit_uniqueid=randomly_generated_unique_id, party_abbreviation='PDP', party_score=request.POST['pdp'])
        AnnouncedPuResults.objects.create(polling_unit_uniqueid=randomly_generated_unique_id, party_abbreviation='DPP', party_score=request.POST['dpp'])
        AnnouncedPuResults.objects.create(polling_unit_uniqueid=randomly_generated_unique_id, party_abbreviation='ACN', party_score=request.POST['acn'])
        AnnouncedPuResults.objects.create(polling_unit_uniqueid=randomly_generated_unique_id, party_abbreviation='PPA', party_score=request.POST['ppa'])
        AnnouncedPuResults.objects.create(polling_unit_uniqueid=randomly_generated_unique_id, party_abbreviation='CDC', party_score=request.POST['cdc'])
        AnnouncedPuResults.objects.create(polling_unit_uniqueid=randomly_generated_unique_id, party_abbreviation='JP', party_score=request.POST['jp'])
        AnnouncedPuResults.objects.create(polling_unit_uniqueid=randomly_generated_unique_id, party_abbreviation='ANPP', party_score=request.POST['anpp'])
        AnnouncedPuResults.objects.create(polling_unit_uniqueid=randomly_generated_unique_id, party_abbreviation='LABOUR', party_score=request.POST['labour'])
        AnnouncedPuResults.objects.create(polling_unit_uniqueid=randomly_generated_unique_id, party_abbreviation='CPP', party_score=request.POST['cpp'])
        return HttpResponseRedirect(reverse('core:index'))
    return render(request, 'core/create_new_polling_unit.html', {
        'all_lga':Lga.objects.all(),
        'all_wards':Ward.objects.all(),
    })