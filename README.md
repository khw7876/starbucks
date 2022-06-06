# starbucks
6월 3일 타임어택 테스트 : 카테고리에 따라 음료를 보는 API 구현</br>
테스트 내용을 재시도해보다가 업그레이드 중입니다...</br>
현재 구현 목표 🔽 </br></br>
<img width="400" alt="스크린샷 2022-06-06 오후 1 51 27" src="https://user-images.githubusercontent.com/104303285/172096964-8fbd819c-e530-4151-a7bc-bfc5d2afd4c7.png"></br></br></br>


버전 2이상 : munu.html & drink.html 사용합니다</br>
* 버전 3 : checkbox 중복 선택하여 해당 카테고리의 음료들을 볼 수 있음</br>
request.POST.get으로 받은 내용을 리스트를 만들어 붙입니다.</br>
선택하지 않은 것은 공백으로 처리합니다.</br>
리스트 축약문을 사용해 공백을 제거해주어 ValueError를 방지합니다.</br>
Image모델에서 타고 들어가 Drink의 category_id와 선택한 것이 맞는지 필터링 합니다.</br>
필터링이 된 내용을 drink.html에 띄워줍니다.</br>
</br></br>
* 버전 2 : checkbox 사용으로 선택된 음료의 이름과 이미지를 볼 수 있음</br>
카테고리를 전부 불러옵니다.</br>
request.POST.get의 값을 카테고리별로 지정해줍니다.</br>
category[2]을 이용해 현재 지정한 카테고리의 id값과 일치하는지 확인해줍니다.</br>
딕셔너리를 만들어 일치하는 값들을 넣어주고 브라우저에 띄워줍니다.</br>
</br></br>
* 버전 1 : 선택한 카테고리의 url로 이동하여 음료의 이름을 볼 수 있음</br>
(product.html & drink0.html)</br>
a태그를 이용하여 각 카테고리의 url로 이동합니다.</br>
장고 기본 템플렛문법을 이용해 선택된 카테고리의 이름들을 보여줍니다.</br>
</br></br>
* 버전 0 : 타임어택 테스트
