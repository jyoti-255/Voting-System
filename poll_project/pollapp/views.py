from django.shortcuts import render, redirect
from .forms import PollForm
from .models import PollModel

def home(request):
    data = PollModel.objects.all()
    return render(request, "home.html", {"data": data})

def create(request):
    if request.method == "POST":
        data = PollForm(request.POST)
        if data.is_valid():
            data.save()
            msg = "Poll created"
            fm = PollForm()
            return render(request, "create.html", {"fm": fm, "msg": msg})
        else:
            msg = "Issue in form submission"
            return render(request, "create.html", {"fm": data, "msg": msg})
    else:
        fm = PollForm()
        return render(request, "create.html", {"fm": fm})

def vote(request, id):
    data = PollModel.objects.get(id=id)
    if request.method == "POST":
        op = request.POST.get("op")
        if op == "op1":
            data.op1c += 1
        elif op == "op2":
            data.op2c += 1
        else:
            data.op3c += 1
        data.save()
        return redirect("home")
    else:
        return render(request, "vote.html", {"data": data})

def result(request, id):
    data = PollModel.objects.get(id=id)
    return render(request, "result.html", {"data": data})
