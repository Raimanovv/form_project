from django.shortcuts import render
from django.views import View
from .forms import GalleryUploadForm
from django.http import HttpResponseRedirect
from .models import Gallery
from django.views.generic.edit import CreateView
from django.views.generic import ListView


class ListGallery(ListView):
    template_name = 'gallery/list_file.html'
    model = Gallery
    context_object_name = 'records'


class CreateGalleryView(CreateView):
    model = Gallery
    # fields = "__all__"
    form_class = GalleryUploadForm
    template_name = 'gallery/load_file.html'
    success_url = 'load_image'

# class GalleryView(View):
#     def get(self, request):
#         form = GalleryUploadForm()
#         return render(request, 'gallery/load_file.html', context={'form': form})
#
#     def post(self, request):
#         form = GalleryUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_file = Gallery(image=request.FILES['image'])
#             new_file.save()
#             return HttpResponseRedirect('load_image')
#         return render(request, 'gallery/load_file.html', context={'form': form})
