# 0602 homework

#### 1. SPA(Single Page Application)과 SFC(Single File Component)의 개념에 대해서 간략하게 작성하시오.

- SPA : 한 페이지에서 모두 일어나는것
- SFA: 한 파일에서 한 컴포넌트



#### 2.  아래 제시된 파일(혹은 폴더)의 역할을 간단하게 작성하시오. 

- router : 경로를 설정해준다.
  - index.js :  
- views : 한 URL에 보이는 페이지
- App.vue : router와 views를 이어주는거.



#### 3.  공식 문서를 참고하여 Vue.js에서 단방향 데이터 흐름을 사용하는 이유에 대해 간략하게 작성하시오

> ​	자식 컴포넌트의 값이 변경되어 부모컴포넌트에 저장된 데이터가 의도치 않게 변경되는 것을 막기 위함이다.



#### 4. 아래의 설명을 읽고 T/F 여부를 작성하시오

- 부모 컴포넌트의 데이터가 새로 갱신되는 경우에 자식 요소의 모든 prop들은 최신 값으로 새로고침된다.
  - True
-  prop으로 전달할 수 있는 데이터는 object만 가능하며 숫자형, 논리 자료형 등은 전달할 수 없다. 
  - False
-  Django와 다르게 Vue.js는 URL을 통해 동적으로 데이터를 전달하는 Variable Routing을 할 수 없다. 
  - False
-  Vue.js 는 Single Page Application이기 때문에 브라우저의 뒤로가기 기능을 지원하지 않는다. 
  - False
-  Vue Router를 사용하면 실제 서버로 요청을 보내지 않고 경로와 연결된 컴포넌트를 보여준다.
  - True

