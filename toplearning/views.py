from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import PdfForm
from .models import Pdf


def home(request):
    contents = {
        'heading': 'Edutech',
        'title': 'Edutech',
    }
    return render(request, 'home.html', context=contents)


def upload(request):
    if request.method == 'Post':  
        form = PdfForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect
    else:
        form = PdfForm()
        
    return render(request, 'upload.html', {'form': form})

def downloads(request):
    books = Pdf.objects.all()
    return render(request, 'downloads.html', {'books': books})
    