# 0601 homework

#### 1. props와emit의 개념과 간단한 설명을 작성하시오.

- props 는 상위 컴포넌트의 데이터를 하위 컴포넌트에서 사용하기 위해서 쓰는 것으로, 단방향으로 데이터를 보내준다.
- emit은 



#### 2. 아래의 설명을 읽고 T/F 여부를 작성하시오..

- Vue CLI 환경에서 Vue 인스턴스의 data 옵션은 반드시 함수의 리턴 값이 객체여야 한다. 
  - False : 함수의 리턴 값이 객체인 것은 컴포넌트일때
- 모든 컴포넌트 인스턴스는 자체 격리 된 범위가 있기 때문에 중첩된 컴포넌트의 관계에서 하위 컴포넌트는 상위 컴포넌트를 직접 참조할 수없으며 그렇게 해서도 안된다. 
  - True 
- 상위 컴포넌트는 props를 통해 하위 컴포넌트에게 이벤트를 보내고 하위 컴포넌트는 emit을 통해 상위 컴포넌트에게 데이터를 전달한다. 
  - False : 두개가 반대로
- 모든 prop들은 부모와 자식 사이에 단방향으로 내려가는 바인딩 형태를 취한다. 이 말은 부모의 속성이 변경되면 자식 속성에게 전달되지만, 반대 방향으로는 전달되지 않는 다는 것을 의미한다.
  - True



#### 3. 다음은 부모 컴포넌트에서 자식 컴포넌트로 데이터를 넘겨주기 위해 작성한 코드의 일부이다. 빈칸 (a), (b)에 들어갈 코드를 작성하시오. (VideoList 컴포넌트는 App 컴포넌트의 자식 컴포넌트이다.)

- (a) = `:videos`    
  - 좌측에 있는것이 props (즉 자식노드에서 쓰이는 변수명이다.)
- (b) =`props`
  - 부모 컴포넌트에 있는 요소를 스기 위해선 props라 쓰고 해야한다.
