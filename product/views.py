from django.shortcuts import redirect, render

from product.models import Category, Drink

# Create your views here.

def drink(request, categories):
    if request.method =='POST':
    
        # drink = Drink.objects.create(name=name, nutrition=nutrition, allergy=allergy, category=category)
        menus = [{'name':'콜드브루'}, {'name':'콜드브루'}, {'name':'콜드브루'}, {'name':'콜드브루'}]
        pick = menus
        context = {
            'name': name,
            'nutrition': nutrition,
            'allergy':allergy,
            'category':category,
    }
    
        # return redirect('/product/')
    # elif request.method == 'GET':
    #     categories = Category.objects.all()
        return render(request, 'product.html', context)    
    