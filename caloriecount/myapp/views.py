from django.shortcuts import render
from .models import Food, Consume
# Create your views here.
def index(request):
    if request.method =="POST":
        food_consumed= request.POST.get('food_consumed')
        food_object= Food.objects.get(pk=food_consumed)
        user= request.user
        consume= Consume(food_consumed= food_object,user= user)
        consume.save()
    foods= Food.objects.all()
    return render(request,'myapp/index.html',{'foods':foods})