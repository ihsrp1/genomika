from django.shortcuts import render
from .models import Disease, User_two
from .forms import DiseaseModelForm, UserModelForm, SignupModelForm
from django.http import HttpResponseRedirect
# Create your views here.

def redirect_view(request, *args, **kwargs):
    return HttpResponseRedirect('/login/')

def signup_view(request, *args, **kwargs):
    form = SignupModelForm()
    ok = False
    if(request.method == 'POST'):
        form = SignupModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = SignupModelForm()
            ok = True
    return render(request, 'signup.html', {'form': form, 'ok': ok})

def login_view(request, *args, **kwargs):
    form = UserModelForm()
    error = False
    if(request.method == 'POST'):
        form = UserModelForm(request.POST or None)
        if form.is_valid():
            given_username = form.cleaned_data['username']
            #print('-------- {} --------'.format(given_username))
            given_password = form.cleaned_data['password']
            #print('-------- {} --------'.format(given_password))
            users_list = User_two.objects.all()
            for u in users_list:
                #print('-------- {} --------'.format(u.username))
                #print('-------- {} --------'.format(u.password))
                if(given_username == u.username and given_password == u.password):
                    error = False
                    return HttpResponseRedirect('/home/')
            form = SignupModelForm()
            
        error = True
    return render(request, 'login.html', {'form':form, 'error': error})

def home_view(request, *args, **kwargs):
    form = DiseaseModelForm()
    m = 'get'
    theones = []
    diseases_list = []
    to_send = []
    if(request.method == 'POST'):
        m = 'post'
        form = DiseaseModelForm(request.POST or None)
        if form.is_valid():
            theones = form.cleaned_data['name'].split('", "')
            theones[0] = theones[0].replace('\"', '')
            theones[-1] = theones[-1].replace('\"', '')
            diseases_list = Disease.objects.all()
            t = 0
            for t in range(len(theones)):
                gene_list = []
                right_name = theones[t]
                equal = False
                for d in diseases_list:
                    if d.name.lower() == theones[t].lower():
                        right_name = d.name
                        equal = True
                        gene_list.append(d.gene)
                st = str(gene_list)[1:-1].replace('\'', '')

                to_send.append([right_name, st, equal])
    
    
    context = {
    'm': m,
    'to_send': to_send,
    'form': form
    }
    return render(request, 'home.html', context)

