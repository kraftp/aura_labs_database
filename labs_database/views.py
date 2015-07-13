from django.shortcuts import render, get_object_or_404

from .models import Lab

# Create your views here.


def index(request):
    labs_list = Lab.objects.order_by('university')
    context = {
        'labs_list' : labs_list,
    }
    return render(request, 'labs_database/index.html', context)

def lab_detail(request, lab_id):
    lab = get_object_or_404(Lab, pk=lab_id)
    return render(request, 'labs_database/lab_detail.html', {'lab': lab})
