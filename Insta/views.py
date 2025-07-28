from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import UserPost

User = get_user_model()

user_id = None

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username_input = request.POST.get('phone_no_or_username_or_email', '').strip()
        password = request.POST.get('password')

        user = authenticate(request, username=username_input, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    footer_links = ['Meta', 'About','Blog','Help','API','Privacy','Term','Locations',
                    'Instagram lite','Threads','Contact Uploading & Non-Users','Meta verified']
    
    return render(request,'auth/login.html',{'footer_links': footer_links})

def logout_view(request):
    print('++++')
    logout(request)
    return redirect('login') 

def register(request):
    if request.method == 'POST':
        mobile_or_email = request.POST.get('mobile_no_or_email')
        password = request.POST.get('password')
        full_name = request.POST.get('full_name')
        username = request.POST.get('user_name')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=mobile_or_email).exists():
            messages.error(request, 'Email already registered')
        else:
            is_phone = mobile_or_email.isdigit() and len(mobile_or_email.strip()) == 10

            user = User.objects.create_user(
                username=username,
                password=password,
                email='' if is_phone else mobile_or_email,
                first_name=full_name
            )

            if is_phone:
                user.phone_number = mobile_or_email
            else:
                user.email = mobile_or_email
            user.save()

            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')
        
    footer_links = [
        'Meta', 'About', 'Blog', 'Help', 'API', 'Privacy', 'Term', 'Locations',
        'Instagram lite', 'Threads', 'Contact Uploading & Non-Users', 'Meta verified'
    ]

    return render(request, 'auth/signup.html', {'footer_links': footer_links})

@login_required(login_url='login')
def home(request):
    return render(request,'home.html',{'is_message_button_required':True})

@login_required(login_url='login')
def user_profile(request, profile_url=None):
    is_not_post = False
    if profile_url:
        if profile_url == 3:
            is_not_post = True
    print('++',request.user.profile_picture)
    return render(request, 'user_profile.html', {
        'no_post_to_show': is_not_post,
        'user_obj': request.user,
        'user_post':request.user.posts.all()
    })


@login_required(login_url='login')
def edit_user_profile(request, user_id=None):
    user = request.user

    if request.method == 'POST':
        # Handle bio update
        if 'bio' in request.POST:
            bio = request.POST.get('bio', '').strip()
            user.bio = bio

        # Handle gender update
        if 'gender' in request.POST:
            gender = request.POST.get('gender', '').strip()
            user.gender = gender

        # Handle website, image, etc., if needed later
        if request.FILES.get('image'):
            image = request.FILES['image']
            user.profile_picture = image

        user.save()
        return redirect('edit_user_profile', user_id=user.id)

    return render(request, 'edit_user_profile/edit_profile.html', {
        'user_details': user
    })

@login_required(login_url='login')
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        user = request.user
        print('+++',user)
        image = request.FILES['image']

        user.profile_picture = image
        user.save()

        image_url = user.profile_picture.url
        
        return JsonResponse({'status': 'success', 'url': image_url})
    
    return JsonResponse({'status': 'error'}, status=400)

@login_required(login_url='login')
def upload_post(request):
    if request.method == 'POST':
       
        user_id = request.user
        user_post_obj = UserPost()
        print('++',user_id)
        user_post_obj.user = user_id
        user_post_obj.post_img = request.FILES.get('post_img')
        user_post_obj.description =  request.POST.get('description')
        user_post_obj.hastags = request.POST.get('hashtags')
        user_post_obj.location = request.POST.get('location')
        user_post_obj.collaborators = request.POST.get('collaborator')
        user_post_obj.is_view_count_likes_hide = request.POST.get('view_count_hide') == 'on'
        user_post_obj.is_comment_section_off = request.POST.get('comment_off') == 'on'

        user_post_obj.save()
        return redirect('user_profile')
