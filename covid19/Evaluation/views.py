from django.shortcuts import render, redirect
from .models import Question


# Create your views here.


def index(request):
    return render(request, 'index.html')


def question(request):
    if request.method == "POST":
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        temperature = request.POST.get('temperature')
        pub_date = request.POST.get('pub_date')
        if float(temperature) > 99.5:
            y = 2
        else:
            y = 0

        vehicle1 = request.POST.get('vehicle1') or 0
        if int(vehicle1) > 1:
            x = 1
        else:
            x = 0

        vehicle2 = request.POST.get('vehicle2') or 0
        if int(vehicle2) > 1:
            x = x+1
        else:
            x = x

        vehicle3 = request.POST.get('vehicle3') or 0
        if int(vehicle3) > 1:
            x = x+1
        else:
            x = x
        vehicle4 = request.POST.get('vehicle4') or 0
        if int(vehicle4) > 1:
            x = x+1
        else:
            x = x
        vehicle5 = request.POST.get('vehicle5') or 0
        if int(vehicle5) > 1:
            x = x+1

        else:
            x = x
        vehicle6 = request.POST.get('vehicle6') or 0

        if int(vehicle6) > 1:
            z = 1
        else:
            z = 0

        vehicle7 = request.POST.get('vehicle7') or 0
        if int(vehicle7) > 1:
            z = z+1
        else:
            z = z

        vehicle8 = request.POST.get('vehicle8') or 0
        if int(vehicle8) > 1:
            z = z+1
        else:
            z = z
        vehicle9 = request.POST.get('vehicle9') or 0
        if int(vehicle9) > 1:
            z = z+1
        else:
            z = z
        vehicle10 = request.POST.get('vehicle10') or 0
        if int(vehicle10) > 1:
            z = z + 1

        vehicle11 = request.POST.get('vehicle11') or 0
        if int(vehicle11) > 1:
            z = z+1
        else:
            z = z
        vehicle12 = request.POST.get('vehicle12') or 0
        if int(vehicle12) > 1:
            z = z+1
        else:
            z = z
        vehicle13 = request.POST.get('vehicle13') or 0
        if int(vehicle13) > 1:
            z = z+1

        else:
            z = z

        if x == 1:
            result = 2+y+(z*2)

        elif x >= 2:
            result = 2+(x-1)+y+(z*2)

        else:
            result = x + y + (z * 2)

        if result < 5:
            a = "Covid-19 Negative"
        elif result >= 5:
            a = "Covid-19 Positive"

        Question.objects.create(
            age=age, gender=gender, temperature=temperature,
            score=result, Covid_Result=a, pub_date=pub_date

        )

        if result < 5:
            return redirect('list1')

        elif result >= 5 and result <= 7:
            return redirect('list2')
        elif result > 7:
            return redirect('list3')

    return render(request, 'question.html')


def view_list1(request):
    obj = Question.objects.all()
    context = {'obj': obj}
    return render(request, 'prescription1.html', context)


def view_list2(request):
    obj = Question.objects.all()
    context = {'obj': obj}
    return render(request, 'prescription2.html', context)


def view_list3(request):
    obj = Question.objects.all()
    context = {'obj': obj}
    return render(request, 'prescription3.html', context)


def result(request):
    obj = Question.objects.all()
    context = {'obj': obj}
    return render(request, 'result.html', context)
