# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Advertisement,UserProfile
from .forms import UserProfileForm

def ads_list(request):
    return redirect('app:home')

def starting_page(request):
    return render(request,"Landing-page/index.html")

def complaint_view(request):
    return render(request,'pages/ui-components.html')

def ad(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        item_name = request.POST.get('item_name')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        cost = request.POST.get('cost')
        category = request.POST.get('category')
        Advertisement.objects.create(image = image,item_name = item_name,description = description,quantity = quantity,cost = cost, category = category,user = request.user)
        return redirect('app:home')
    else:
        return render(request,"pages/new-post.html")

@login_required(login_url="{%url 'authentication:login'%}")
def home(request):
    ad = Advertisement.objects.all()
    for i in ad:
        print(i.image)
    args ={
        'ad':ad,
    }
    return render(request, "pages/blog-posts.html", args)

def profile(request):
    userprofile,created = UserProfile.objects.get_or_create(user = request.user)
   
    if request.method == 'POST':
      
        user_profile = UserProfileForm(request.POST, request.FILES,instance = userprofile)
        if user_profile.is_valid():
            user_profile.save()
            return redirect('app:home')
    
        else:
            return redirect('app:profile')

    else:
        profile_form = UserProfileForm(instance = userprofile)
        return render(request, 'pages/user-profile.html', {'form':profile_form, 'user':request.user})











@login_required(login_url="{%url 'authentication:login%}")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))

