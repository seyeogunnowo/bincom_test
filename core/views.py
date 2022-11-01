from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def polling_units_results(request):
    if request.method=='POST':
         return render(request, 'core/polling_units_results.html', {
        'all_pu':PollingUnit.objects.all(),
        'selected_pu_id':request.POST['polling_unit'],
        'pu_results':AnnouncedPuResults.objects.all()

    })
    return render(request, 'core/polling_units_results.html', {
        'all_pu':PollingUnit.objects.all(),
    })

def lga_sum_results(request):
    if request.method=='POST':
        apr_data={}
        for pu in PollingUnit.objects.all():
          if pu.lga_id == request.POST['lga']:
            for apr in AnnouncedPuResults.objects.all():
                if apr.polling_unit_uniqueid == pu.uniqueid:
                    for apr_party in apr:
                        apr_data[apr_party.party_abbreviation]=apr_party.party_score
        print(apr_data)
        return render(request, 'core/lga_sum_results.html', {
        'all_lga':Lga.objects.all(),

    })
    return render(request, 'core/lga_sum_results.html', {
        'all_lga':Lga.objects.all(),
    })