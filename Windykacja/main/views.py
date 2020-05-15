from django.shortcuts import get_object_or_404, render, redirect
from .forms import User, SignUpForm
from .models import Profile, Case, Dokument
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


@login_required
def pomoc(request):
    return render(request, 'pomoc.html')


@login_required
def sprawy(request):
    users = User.objects.all()
    cases = Case.objects.all()
    return render(request, 'sprawy.html', {'cases': cases, 'users': users})


@login_required
def sprawa(request, id):
    users = get_object_or_404(User, pk=id)
    users.save()
    cases = get_object_or_404(Case, pk=id)
    cases.save()
    documents = Dokument.objects.all()

    return render(request, 'sprawa.html', {'users': users, 'cases': cases, 'documents': documents})

@login_required
def profil(request):
    info = Profile.objects.all()
    cases = Case.objects.all()
    return render(request, 'index.html', {'info': info, 'cases': cases})


@login_required
def windykatorzy(request):
    basic_info = User.objects.all()
    extra_info = Profile.objects.all

    return render(request, 'windykatorzy.html', {'basic_info': basic_info, 'extra_info': extra_info})


@login_required
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.worker_number = form.cleaned_data.get('worker_number')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.image = form.cleaned_data.get('image')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/windykatorzy/')
    else:
        form = SignUpForm()
    return render(request, 'nowypracownik.html', {'form': form})


@login_required
def edit_worker(request, id):
    user = get_object_or_404(User, pk=id)
    form = SignUpForm(request.POST or None, request.FILES or None, instance=user)

    if form.is_valid():
        user = form.save()
        user.refresh_from_db()  # load the profile instance created by the signal
        user.profile.worker_number = form.cleaned_data.get('worker_number')
        user.profile.phone = form.cleaned_data.get('phone')
        user.profile.image = form.cleaned_data.get('image')
        user.save()
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=raw_password)
        login(request, user)
        return redirect('/windykatorzy.html/')

    return render(request, 'editworker.html', {'form': form})






@login_required
def delete_worker(request, id):
    user = get_object_or_404(User, pk=id)

    if request.method == 'POST':
        user.delete()
        return redirect('/windykatorzy/')

    return render(request, 'confirm.html', {'user': user})


@login_required
def delete_documents(request, id):
    document = get_object_or_404(User, pk=id)

    if request.method == 'POST':
        document.delete()
        return redirect('/sprawa/<id>/')

    return render(request, 'close.html', {'document': document})


@login_required
def newcase(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.worker_number = form.cleaned_data.get('worker_number')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.image = form.cleaned_data.get('image')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/windykatorzy/')
    else:
        form = SignUpForm()
    return render(request, 'nowypracownik.html', {'form': form})