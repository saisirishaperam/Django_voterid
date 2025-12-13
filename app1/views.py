from django.shortcuts import render, get_object_or_404
from app1.models import vote
from app1.form import voter_form
import random, string
# from django.contrib.auth.decorators import login_required

# Create your views here.

def fronhome(request):

    return render(request, 'home.html')

def detals(request):
    form = voter_form()
    context = {
        'form' : form
    }
    return render(request, 'form.html', context)


# @login_required(login_url='login')

ADMIN_PASSWORD = '1234'
def cards(request):
    if request.method == 'POST':
        if request.POST.get('admin_pass') != ADMIN_PASSWORD:
            form = voter_form(request.POST, request.FILES)
            form.add_error(None, "Invalid password. Access denied.")
            return render(request, 'form.html', {'form': form})


        form = voter_form(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()

            #Genertae unque voter id
            obj.voter_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
            obj.save()
            return render(request, 'card.html', {'data' : obj})
        else:

            return render(request, 'form.html', {'form' : form})
        
    # form = voter_form()
    # return render(request, 'card.html', {'data' : obj})

def lst_vote(request):
    data = vote.objects.all()
    context = {
        'data' : data
    }

    return render(request, 'list.html', context)

def getvoter(request,id):
        voter = get_object_or_404(vote, id=id)
        return render(request, 'card.html', {'data' : voter})
    