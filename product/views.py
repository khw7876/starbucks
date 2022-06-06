from nis import cat
from unicodedata import category
from django.shortcuts import redirect, render
from product.models import Category, Drink, Image

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 버전 3 - checkbox 다중 선택 가능 #

def menu(request):
    if request.method == 'GET':
        return render(request, 'menu.html')
    
    elif request.method == 'POST':
        print(request.POST)
        # <QueryDict: {'csrfmiddlewaretoken': ['zAOvKMYmMQuaa9Xwm0IzfaO9H7QiC0nc3vwo4AXE2Mk7L4dkZHHKUYUQj42PrNPj'], 'coldbrew': ['1'], 'blended': ['4']}>
        
        category_list = []
        
        category_list.append(request.POST.get('coldbrew', ''))
        category_list.append(request.POST.get('brewed', ''))
        category_list.append(request.POST.get('espresso', ''))
        category_list.append(request.POST.get('blended', ''))
        # checkbox 선택하지 않을때 ''으로 표시 > ['1', '', '', '4']
        # >밑에서 name__category_id와 category_list 필터시 id자리에 숫자가 와야하는데 공백이 올 경우 ValueError 발생 
        
        category_list = [x for x in category_list if x]
        print(category_list)
        # list 축약문으로 리스트에 있는 공백요소 제거['1', '4']
        
        images = Image.objects.filter(name__category_id__in=category_list)
        print(images)
        # Image 의 name > "__" 뜻: Drink FK를 타고 들어감>Drink의 category_id 가 되는 것임!
        # __in 은 리스트 안에 포함되어 있는지 확인할때 씀
        # <QuerySet [<Image: 바닐라 크림 콜드 브루>, <Image: 콜드 브루>, <Image: 콜드 브루 몰트>, <Image: 콜드 브루 오트 라떼>, <Image: 콜드 브루 플로트>, <Image: 돌체 콜드 브루>, <Image: 나이트로 바닐라 크림>, <Image: 망고 패션 프루트 블렌디드>, <Image: 딸기 딜라이트 요거트 블렌디드>, <Image: 망고 바나나 블렌디드>, <Image: 민트 초콜릿 칩 블렌디드>, <Image: 트위스트 피치 요거트 블렌디드>, <Image: 피치 & 레몬 블렌디드>]>
        
        return render(request, 'drink.html', {'images':images})
        # 딕셔너리를 담아서 브라우저에 띄워주기

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 버전 2 #

# def menu(request):
#     if request.method == 'GET':
#         return render(request, 'menu.html')
    
#     elif request.method == 'POST':
#         # category = {'coldbrew':'콜드 브루 커피','brewed':'브루드 커피', 'espresso':'에스프레소', 'blended':'블렌디드'}
#         # print(request.POST)
#         category = Category.objects.all()
        
#         if request.POST.get('coldbrew'):
#             print(f'여기1')
#             category = Category.objects.get(name=category[0])
#             # category = Category.objects.get(name=category['coldbrew'])
#             print(f'카테고릐루리ㅣ리리리ㅣ{category}')
            
#             images = Image.objects.filter(name__category_id=category)
#             print(f'이미지 링크 받아오나요{images}')
            
#             menu = {
#                 'images':images
#             }
#             # for image in images:
#             #     print(image.url)
#             #     print(image.name.name)
#             #     print(image.name.nutrition)
#             #     print(image.name.allergy)
#             #     break
#             return render(request, 'drink.html', menu)
        
#         elif request.POST.get('brewed'):
#             category = Category.objects.get(name=category[1])
#             images = Image.objects.filter(name__category_id=category)
              
#             menu = {
#                 'images':images
#             }
            
#             return render(request, 'drink.html', menu)
              # # brewed를 선택했을때.
              # # caterogy 모델의 name이 위에서 선언한 category~all()에서 두번째 조건과 맞는지 확인-admin에서 카테고리 생성했을때 id번호와 맞는지
              # # Image 모델의 name의 FK를 ("__" 뜻:) 타고 들어감 > Drink의 category_id와 category[1]과 맞는지 (둘다 숫자)
              # # menu라는 딕셔너리를 만들어서 images를 담아주고 브라우저에 같이 띄워주기  
        
#         elif request.POST.get('espresso'):
#             category = Category.objects.get(name=category[2])
#             images = Image.objects.filter(name__category_id=category)
            
#             menu = {
#                 'images':images
#             }
            
#             return render(request, 'drink.html', menu)
        
#         elif request.POST.get('blended'):
#             category = Category.objects.get(name=category[3])
#             images = Image.objects.filter(name__category_id=category)
            
#             menu = {
#                 'images':images
#             }
            
#             return render(request, 'drink.html', menu)
            



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 버전 1 #


# def drink(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         return render(request, 'product.html', {'categories':categories})  


    
# def search(request, id):
#     if request.method == 'GET':
        
#         category = Category.objects.get(id=id)
#         categories = Category.objects.all()
#         print(f'이거는 category {category}')
        
#         drinks = Drink.objects.filter(category=category)
#         print(f'이름을 프린트합니다{drinks}')

#         return render(request, 'drink0.html', {'drinks':drinks, 'categories':categories})
    
#     elif request.method =='POST':
#         return render(request, 'product.html')