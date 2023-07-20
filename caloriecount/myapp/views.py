from django.shortcuts import render,redirect
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
    else:
        
        #consumed_foods= Consume.food_consumed_set()
        foods= Food.objects.all()
    consumed_foods= Consume.objects.filter(user= request.user)

    return render(request,'myapp/index.html',{'foods':foods,'consumed_foods': consumed_foods })

def delete_consume(request,id):
    consumed_food= Consume.objects.get(pk= id)
    if request.method=="POST":
        consumed_food.delete()
        return redirect("/")
    else:
        
        return render(request,'myapp/delete.html',{'food':consumed_food})