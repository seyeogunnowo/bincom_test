from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='core'

urlpatterns=[
    path('', views.index, name='index'),
    path('polling-units-results', views.polling_units_results, name='polling_units_results'),
    path('lga-sum-results', views.lga_sum_results, name='lga_sum_results'),
]

urlpatterns += staticfiles_urlpatterns()