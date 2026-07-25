from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import LoginForm
from .forms import RegistrationForm
from .models import PortfolioProject,News,Trending
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    trending_games = Trending.objects.all()[:8]   # Eng ko'p 8 ta
    return render(request, "index.html", {
        'trending_games': trending_games
    })

   
def home(request):
    return render(request,'home.html')  





def news(request):
    news_list = News.objects.filter(is_published=True).order_by('-created_at')
    return render(request, "news.html", {'news_list': news_list})
def about(request):
    return render(request,"about.html")
def portfolio(request):
    projects = PortfolioProject.objects.all()
    return render(request, "Portfolio.html", {'projects': projects})
def contact(request):   
    return render(request,"contact.html")
def login_form(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)
            messages.success(request, "Muvaffaqiyatli o'tdingiz")

            return redirect('index')
        else:
            messages.error(request, "login yoki parol xato")

            return redirect('login')
    else:
        return render(request, "login.html",{"form" : form})


def logout_user(request):
    logout(request)
    messages.success(request, "Tizimdan chiqdingiz")

    return redirect('login')

def  register_view(request):
    if request.method == "POST":
    
        form = RegistrationForm(request.POST)
        # agar from malumotlari togri bolsa
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            User.objects.create_user(
                username=username,
                password=password
            )       
            messages.success(request,"muvaffaqiyatli royhatdan otdingiz")
            return redirect('index')
        else:
            messages.error(request,"Forma notogri kiritilgan")
    else:
        form = RegistrationForm()

    return render(request,"register.html", {"form" : form})


 