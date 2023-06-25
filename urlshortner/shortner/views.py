from django.shortcuts import render
import uuid
from .models import Url
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(f'https://' + url_details.link)

def redirect_view(request, shortened_url):
    full_url = Url.objects.get(shortened_url=shortened_url).full_url
    return redirect(full_url)
