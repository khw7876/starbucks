from unicodedata import category
from django.shortcuts import redirect, render
from product.models import Category, Drink, Image

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 버전 2 #

def menu(request):
    if request.method == 'GET':
        return render(request, 'menu.html')
    
    elif request.method == 'POST':
        # category = {'coldbrew':'콜드 브루 커피','brewed':'브루드 커피', 'espresso':'에스프레소', 'blended':'블렌디드'}
        # print(request.POST)
        category = Category.objects.all()
        
        if request.POST.get('coldbrew'):
            print(f'여기1')
            category = Category.objects.get(name=category[0])
            # category = Category.objects.get(name=category['coldbrew'])
            print(f'카테고릐루리ㅣ리리리ㅣ{category}')
            
            images = Image.objects.filter(name__category_id=category)
            print(f'이미지 링크 받아오나요{images}')
            
            menu = {
                'images':images
            }
            # for image in images:
            #     print(image.url)
            #     print(image.name.name)
            #     print(image.name.nutrition)
            #     print(image.name.allergy)
            #     break
            return render(request, 'drink.html', menu)
        
        elif request.POST.get('brewed'):
            category = Category.objects.get(name=category[1])
            images = Image.objects.filter(name__category_id=category)
            
            menu = {
                'images':images
            }
            
            return render(request, 'drink.html', menu)
        
        elif request.POST.get('espresso'):
            category = Category.objects.get(name=category[2])
            images = Image.objects.filter(name__category_id=category)
            
            menu = {
                'images':images
            }
            
            return render(request, 'drink.html', menu)
        
        elif request.POST.get('blended'):
            category = Category.objects.get(name=category[3])
            images = Image.objects.filter(name__category_id=category)
            
            menu = {
                'images':images
            }
            
            return render(request, 'drink.html', menu)
            



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 버전 1 #


def drink(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'product.html', {'categories':categories})  


    
def search(request, id):
    if request.method == 'GET':
        
        category = Category.objects.get(id=id)
        categories = Category.objects.all()
        print(f'이거는 category {category}')
        
        drinks = Drink.objects.filter(category=category)
        print(f'이름을 프린트합니다{drinks}')

        return render(request, 'drink0.html', {'drinks':drinks, 'categories':categories})
    
    elif request.method =='POST':
        return render(request, 'product.html')