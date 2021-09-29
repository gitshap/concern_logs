from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from concerns.models import Concerns, Name
from concerns.forms import ConcernCreationForm
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


import csv


def export_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    concern = Concerns.objects.get(id=33)
    p.drawString(200, 700, concern.person)
    p.drawString(300, 700, concern.findings)
    p.drawString(400, 700, concern.status)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv/force-download',
        headers={'Content-Disposition': 'attachment; filename="report.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['Person', 'Problem', 'Resolution',
                    'Status', 'Notes', 'Created At', 'Updated_at'])
    for concern in Concerns.objects.all().values_list('person', 'problem', 'resolution', 'status', 'additional_notes', 'created_at', 'updated_at'):
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


def hello_view(request, name):

    if Name.objects.filter(name=name).exists():
        return HttpResponse('User has already been created ' + name)
    else:
        Name.objects.create(name=name)

    return HttpResponse(name, ' has been created')
