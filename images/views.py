from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image,Category,Location
import pyperclip

# Create your views here.

def welcome(request):
        '''
        a function to display the whole images and welcome message.
        '''

        images = Image.get_all_images()
        return render(request, 'welcome.html', {"images":images})

def search_image(request):
        '''
        a function to search image based on their categories.
        '''

        categories = Category.objects.all()
        if 'image' in request.GET and request.GET['image']:
                category_item = request.GET.get('image')
                searched_image = Image.search_by_category(category_item)
                message = f"{category_item}"

                return render(request, 'search.html', {"images":searched_image,"message":message, "categories":categories})

        else:
                message = "You have not search for any item"
        return render(request, 'search.html', {"message": message})

def image_location(request,location_id):
        '''
        a function to filter image by location.
        '''

        location_of_image = Image.filter_by_location(location_id)
        return render(request,'location.html', {"location_of_image":location_of_image})

def image(request,image_id):
        '''
        a funtion to display single image.
        '''

        try:
                image = Image.objects.get(id = image_id)
        except DoesNotExist:
                raise Http404()
        return render(request, 'images.html', {"image":image})

def copy_image_url(request, image_id):
        '''
        a function to copy image link.
        '''

        images = Image.get_all_images()
        loc = Image.objects.get( id = image_id)
        pyperclip.copy('http://127.0.0.1:8000/' + loc.pic_image.url)
        pyperclip.paste()
        return render(request, 'welcome.html', {"images":images})
