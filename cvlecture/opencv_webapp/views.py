from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage


def first_view(request):
    return render(request, 'opencv_webapp/first_view.html', {})

def uimage(request):
    form = None
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
    if form is not None and form.is_valid():
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'opencv_webapp/uimage.html', {'form': form, 'uploaded_file_url': uploaded_file_url})
    else:
        form = UploadImageForm()
        return render(request, 'opencv_webapp/uimage.html', {'form': form})