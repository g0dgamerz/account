from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Laddger
from .models import Journal
from django.views.generic import TemplateView
from .forms import registerForm,EditForm
from django.urls import reverse


def home(request):
	return render(request,'base.html')
def journal(request):
	data = Laddger.objects.all()
	return render(request, 'journal.html', {'account_data':data})
def journaldetails(request,detail):
	data = [c.account_name for c in Laddger.objects.all()]
	if detail in data:
		a=detail 
		tab = Journal.objects.filter(Accounthead__account_name=a)
		totalamount = 0
		balancingamount = 0
		finalamount = 0
		finalamount =[]
		dramount=[]
		cramount=[]
		for i in tab:
			totalamount=(i.Debit-i.Credit)
			dramount.append(i.Debit)
			cramount.append(i.Credit)
			balancingamount=balancingamount+totalamount
			finalamount.append(balancingamount)
		f=finalamount
		g=balancingamount
		return render(request,'journaldetails.html',{'tab':tab,'nam':detail,'list':f,'list2':g})

def add_account(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('journal'))
    else:
        form = registerForm()
        args={'form':form}
        return render(request,'addacc.html',args)

def edit(request,id):
    item=Journal.objects.get(id=id)
    if request.method == 'POST':
        form = EditForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect(reverse('journal'))
    else:
        form = EditForm(instance=item)
        c = {'form':form}
        return render(request,'edit.html',c)

def destroy(request, id):
    item = Journal.objects.get(id=id)
    item.delete()
    return redirect('journal')
