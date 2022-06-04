from django.shortcuts import redirect, render

from product.models import Category, Drink, Image

# Create your views here.

def drink(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'product.html', {'categories':categories})  


    
def search(request, id):
    if request.method == 'GET':
        
        category = Category.objects.get(id=id)
        categories = Category.objects.all()
        print(f'이거는 category 포스트여{category}')
        
        drinks = Drink.objects.filter(category=category)
        print(f'이름을 프린트합니다{drinks}')

        return render(request, 'drink.html', {'drinks':drinks, 'categories':categories})
    
    elif request.method =='POST':
        return render(request, 'product.html')
    
