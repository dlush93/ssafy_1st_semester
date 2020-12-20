# 0609_homework



1. MVVM은 무엇의 약자인지 작성하시오

   Model View ViewModel



2. 아래의 설명을 읽고 T/F 여부를 작성하시오. 

   - Vue.js에서 반응형은 data가 변경되면 이에 반응하여 연결된 DOM이 다시 렌더링 되는 것을 의미한다. 
     - True
   -  동일한 노드에 v-for, v-if 두 디렉티브가 함께 있다면 v-if가 더 높은 우선 순위를 가 진다. 
     - False
   -  npm은 Node Package Manager의 약자로 자바스크립트 런타임 환경 Node.js의 기 본 패키지 관리자이다. 
     - True
   -  Vue 인스턴스는 Vue 컴포넌트이며 .vue 확장자를 통해 SFC를 용이 하게 구현할 수 있다. 
     - True
   -  컴포넌트에서 data는 반드시 object를 리턴해야한다.
     - True 

   - 상태 관리 패턴은 어떤 경우에도 최적화 되어 있기 때문에 SPA 개발을 한다면 항상 숙지하여 사용해야한다.
     - False

3. 아래는 Vue Router와 관련된 코드이다. 빈칸에 들어갈 코드를 작성하시오.

   - `(a) = /lunch`
   - `(b) = router-link`
   - `(c) = router-view`



4. 아래의 코드에서 increment 메서드가 실행될 때 단방향 데이터 흐름에 대해서 설명하시오. (Action, State, View의 관점에서 설명하시오.)
   - increment 액션이 들어오면 methods로 들어간다. 거기서 increment의 메소드 액션을 실행한다.
   - 해당 메소드 안에서 상태에 접근을 하므로, data의 count를 증가시켜서 변경시켜준다.
   - 그리고 마지막으로 View에서 보간법으로 count의 데이터를 불러온다.