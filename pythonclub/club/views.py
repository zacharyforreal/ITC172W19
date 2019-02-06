from django.shortcuts import render
from .models import Resource

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def resource (request):
    resource_list=Resource.objects.all()
    return render (request, 'club/resource.html', {'resource_list': resource_list})

def getmeetings (request):
    meeting_list=Meeting.objects.all()
    return render (request, 'club/meetings.html', {'meeting_list': meeting_list})

def meetingdetail(request, id):
    detail=get_object_or_404(Product, pk=id)
    context = { 'detail': detail}
    return render (request, 'club/details.html',context=context )

