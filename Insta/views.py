from django.shortcuts import render

# Create your views here.
def login(request):
    footer_links = ['Meta', 'About','Blog','Help','API','Privacy','Term','Locations',
                    'Instagram lite','Threads','Contact Uploading & Non-Users','Meta verified']
    
    return render(request,'auth/login.html',{'footer_links': footer_links})

def register(request):
    footer_links = ['Meta', 'About','Blog','Help','API','Privacy','Term','Locations',
                    'Instagram lite','Threads','Contact Uploading & Non-Users','Meta verified']
    return render(request,'auth/signup.html',{'footer_links': footer_links})

def home(request):
    return render(request,'home.html',{'is_message_button_required':True})