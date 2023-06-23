from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Conference

def conf_list(request):
    conferences = Conference.objects.all()
    return render(request, 'conference/conf_list.html')

def conf_create(request):
    return render(request, 'conference/conf_create.html')

def conf_details(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    return render(request, 'conference/conf_details.html')

def conf_update(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    return render(request, 'conference/conf_update.html')

def conf_delete(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
return render(request, 'conference/conf_delete.html)
