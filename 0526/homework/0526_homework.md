# 0526_homework

1.  computed와 watch의 개념과 그 차이에 대해서 간략하게 설명하시오.
   - watch : 변수를 계속 바라보면서 변화가 감지가 되면 내부의 함수를 실행한다.
   - computed : 변수를 만들어놓고 값을 저장하고, 그 변수에 저장된 값이 변경될때 변경해서 저장한다.
2.  
   -  동일한 노드에 v-for와 v-if, 두 디렉티브가 함께 있다면 v-if가 더 높은 우선 순위를 가지며, v-if는 루프가 반복 될 때마다 실행된다. 
   
     - False (v-for이 더 우선순위가 크다.)
   - Vue.js에서 HTML 속성에 Interpolation(보간법) 형태로 값을 넣을 수 있지만 코드 작성의 통일성을 위해 v-bind 디렉티브를 사용한다.
   
     - False (보간법 불가능)
   -  v-bind 디렉티브는 “ @ “, v-on 디렉티브는 “ : ” shortcut(약어)을 제공한다.
   
     - False (반대로 되어 있다.)
   - v-model 디렉티브는 input, textarea, select 같은 HTML Element와 단방향 데이터 바인딩을 이루기 때문에 v-model 속성값의 제어를 통해 값을 바꿀 수 있다.
   
     - False (양방향 바인딩이다.)
3.  
   - (a) : v-for
   - (b) : v-if
   - (c) : {{number}}
   - (d) : data

