from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import URL
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import json
import string
import random


def home(request):
    return render(request, 'main/home.html')


@csrf_exempt
def url_shortener(request):
    if request.method == 'POST':
        long_url = request.POST.get("long_url")

        if "://" not in long_url:
            long_url = 'http://' +long_url
        
        try:
            validate = URLValidator(schemes=['http', 'https'])
            validate(long_url)
        except ValidationError:
            data = {"error": "Please enter a valid link."}
            response = HttpResponse(json.dumps(data),
                                    content_type="application/json")
        
            response.status_code = 400
            return response
        # Checking if a shortened-url already exists 
        # in database for this long url
        record = URL.objects.filter(original_url=long_url)
        if record.exists():
            suffix = record.first().shortened_suffix
            domain = request.META['HTTP_ORIGIN']
            short_url = f"{domain}/{suffix}"
            
        else:
            N = 6  
            UNIQUE = False
            
            while UNIQUE is False:
                # using random.choices() 
                # generating random strings  
                suffix = ''.join(random.choices(string.ascii_lowercase +string.ascii_uppercase +
                                             string.digits, k = N))
                try:
                    # Saving url record
                    URL.objects.create(original_url=long_url, shortened_suffix=suffix)
                    UNIQUE = True
                except IntegrityError as e:
                    if 'UNIQUE constraint failed' in e.args[0]:
                        continue
                    else:
                        messages.error(request, "An error occurred. Please try again.")
                        return redirect('/')
                        break


            domain = request.META['HTTP_ORIGIN']
            short_url = f"{domain}/.{suffix}"
        
        
        response = {
            "shortUrl": short_url
        }

        return  HttpResponse(json.dumps(response))

    messages.error(request, "An error occurred. Please try again.")
    return redirect('/')


def url_redirect(request, suffix=None):
    if suffix is not None:
        suffix = '.' +suffix
        record = URL.objects.filter(shortened_suffix=suffix)

        if record.exists():
            return redirect(record[0].original_url)

        else:
            messages.error(request, "No matching shortened-url found.")
            return redirect('/')

