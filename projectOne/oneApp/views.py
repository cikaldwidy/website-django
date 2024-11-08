from django.shortcuts import render
from django.http import HttpResponse
from oneApp.models import Topic, Webpage,AccesRecord
# Create your views here.
#request dan respons
def index(request):
    webpages_list = AccesRecord.objects.order_by('date')
    date_dict={'access_records':webpages_list}
    return render(request, 'firstApp/index.html',context=date_dict)
