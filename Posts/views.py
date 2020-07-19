from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Neighborhood,Profile,Business,Notice,HealthCenter,Police
from .forms import CreateHoodForm,UpdateProfileForm,SubmitBusinessForm,ShareNoticeForm,AddBusinessForm,AddNeighborhoodForm,JoinNeighborhoodForm




#landing/index page
def index(request):
    health_centers=HealthCenter.objects.all()
    police_stations=Police.objects.all()
    
    return render(request,'index.html', locals())


#profilePage
def myProfile(request):
    userProfile = Profile.objects.all()
    userNotices = Notice.objects.filter(user=request.user)
    notices=Notice.objects.all()

    return render(request, 'posts/profile.html', locals())


#updateProfile
def updateProfile(request):
    my_prof = Profile.objects.get(user=request.user)
 
    if request.method == 'POST':
        updateProf = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)

        if updateProf.is_valid():
            updateProf.save()
              
        return redirect('my_profile')
    else:
        updateProf = UpdateProfileForm(instance=request.user.profile)
    
    return render(request, 'posts/update_profile.html', locals())


#neighborhoods/join a neighborhood
@login_required(login_url='/accounts/login')
def neighborhood(request):
    neighborhoods=Neighborhood.objects.all()
    form = AddNeighborhoodForm()
    joinForm = JoinNeighborhoodForm()
     
    return render(request,'posts/neighborhoods.html', locals())


#add a neighborhood
def addNeighborhood (request):
    form = AddNeighborhoodForm()
    joinForm = JoinNeighborhoodForm()

    
    if request.method == 'POST':
        form = AddNeighborhoodForm(request.POST,request.FILES)
        user = request.user.id
        
        if form.is_valid():
            neighborhood = form.save(commit=False)
            neighborhood.user = request.user
            neighborhood.save()
        return redirect('view_neighborhoods')
    else:
        form = AddNeighborhoodForm()
        joinForm = JoinNeighborhoodForm(instance=request.user.profile)

        return render(request, 'posts/neighborhoods.html', locals())


#join neighborhood
def joinNeighborhood(request, neighborhood_id):
    joinForm = JoinNeighborhoodForm()
    
    if request.method == 'POST':
        joinForm = JoinNeighborhoodForm(request.POST,request.FILES, instance=request.user.profile)
        neighborhood = get_object_or_404(Neighborhood,pk=neighborhood_id)
        if joinForm.is_valid():
            new_occupant = joinForm.save(commit=False)
            new_occupant.user = request.user
            new_occupant.save()
        return redirect('view_notices', neighborhood_id)


#share a notice
@login_required(login_url='/accounts/login')
def shareNotice(request, neighborhood_id):
    form = ShareNoticeForm()
    
    if request.method == 'POST':
        form = ShareNoticeForm(request.POST,request.FILES)
        user = request.user.id
        
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.user = request.user
            announcement.save()
        return redirect('view_notices', neighborhood_id)
    else:
        form = ShareNoticeForm()
        return render(request, 'posts/share_notice.html', locals())
    

#view notices/alerts/announcements
@login_required(login_url='/accounts/login')
def viewNotices(request, neighborhood_id):
    notices=Notice.objects.all()
    neighborhood = get_object_or_404(Neighborhood,pk=neighborhood_id)
    neighborhoodNotices = Notice.objects.filter(neighborhood=neighborhood)
    print(notices, "=====ALL NOTICES======")
    print(notices, "======RESPECTIVE HOOD NOTICES=====")

    return render(request,'posts/notices.html', locals())


#view businesses
@login_required(login_url='/accounts/login')
def business(request):
    businesses=Business.objects.all()
    form = AddBusinessForm()
    
    return render(request,'posts/businesses.html', locals())


#add a business
def addBusiness (request):
    form = AddBusinessForm()
    
    if request.method == 'POST':
        form = AddBusinessForm(request.POST,request.FILES)
        user = request.user.id
        
        if form.is_valid():
            business = form.save(commit=False)
            business.user = request.user
            business.save()
        return redirect('view_businesses')
    else:
        form = AddBusinessForm()
        return render(request, 'posts/businesses.html', locals())

#search businesses
@login_required(login_url='/accounts/login')
def searchBusiness(request):

    if 'search' in request.GET and request.GET["search"]:
    
        search_term = request.GET.get("search")
        searched_businesses = Business.objects.filter(bsns_name__icontains=search_term)
        message = f"{search_term}"
        
        return render(request, 'posts/search_results.html', locals())
    
    else:
        
        message = "you haven't searched for any business"  
        return render(request, 'posts/search_results.html', locals())
    

#view health centers
def healthCenters(request, neighborhood_id):
    neighborhood = get_object_or_404(Neighborhood,pk=neighborhood_id)
    health_centers = HealthCenter.objects.filter(neighborhood=neighborhood)
    
    return render(request,'posts/health_centers.html', locals())


#view police stations
def policeStations(request, neighborhood_id):
    neighborhood = get_object_or_404(Neighborhood,pk=neighborhood_id)
    police_stations = Police.objects.filter(neighborhood=neighborhood)
    
    return render(request,'posts/police_stations.html', locals())