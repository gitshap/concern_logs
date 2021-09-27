from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from concerns.models import Concerns
from concerns.forms import ConcernCreationForm
from django.template import loader

import csv

def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['Person', 'Findings', 'Resolution', 'Status', 'Created At', 'Updated_at'])
    for concern in Concerns.objects.all().values_list('person','findings','resolution','status','created_at','updated_at'):
        writer.writerow(concern)

    return response


def home(request):
    concerns = Concerns.objects.all()
    form = ConcernCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            concern = form.save(commit=False)
            concern.id = request.POST.get('id')
            concern.save()
            return redirect("concern-detail", pk=concern.id)
        else:
            return render(request, 'concern_form.html',
                          context={
                              "form": form
                          })

    context = {
        'form': ConcernCreationForm,
        'concerns': concerns
    }
    template_name = 'home.html'
    concerns = Concerns.objects.order_by('-created_at')

    context = {
        'concerns': concerns
    }
    return render(request, template_name, context=context)

# for cancelling extra forms


def empty(request):
    template_name = 'empty.html'
    return render(request, template_name, context=None)


def create_concern_form(request):
    form = ConcernCreationForm()
    context = {
        "form": form
    }
    return render(request, "concern_form.html", context)


def create_concern(request):
    concerns = Concerns.objects.all()
    form = ConcernCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            concern = form.save(commit=False)
            concern.id = request.POST.get('id')
            concern.save()
            return redirect("concern-detail", pk=concern.id)
        else:
            return render(request, 'concern_form.html',
                          context={
                              "form": form
                          })

    context = {
        'form': ConcernCreationForm,
        'concerns': concerns
    }

    template_name = 'create_concern.html'
    return render(request, template_name, context=context)


def concern_detail(request, pk):
    concerns = get_object_or_404(Concerns, id=pk)
    context = {
        "concerns": concerns
    }
    return render(request, "concern_detail.html", context)


def update_concern(request, pk):
    concerns = Concerns.objects.get(id=pk)
    form = ConcernCreationForm(request.POST or None, instance=concerns)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(concern_detail, pk=concerns.id)

    context = {
        "form": form,
        "concerns": concerns
    }

    return render(request, "concern_form.html", context)


def delete_concern(request, pk):
    concern = get_object_or_404(Concerns, id=pk)

    if request.method == "POST":
        concern.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )
