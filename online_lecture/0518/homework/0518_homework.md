# 0518_homework



#### 1.  DOM에서 특정 요소를 선택할 때, document.querySelector() 뿐만 아니라 document.querySelectorAll() 역시 사용 할 수 있다. 이 둘의 차이를 간단하게 작성하시오.

> 반환 하는 데이터 타입이 다르다.
>
> querySelector()는 없으면 null을 반환하고, 여러개가 있을때에는 최상위 하나만 반환한다.
>
> document.querySelectorAll()  은 여러개를 반환한다.



#### 2.DOM에 요소를 추가할 때, innerHTML 속성을 사용하는 방법과 appendChild() 메서드를 사용하는 방법이 있다. 이 둘의 차이를 간단하게 작성하시오.

> innerHTML 은 태그까지 직접 적어줘야하고 스트링으로 넣어줘야한다.
>
> appendChild는 자식노드를 넣어주는 거다 .





#### 3. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- 콜백 함수는 주로 동기식 처리 모델에 사용된다. (F)

-  콜백 함수는 매개 변수를 통해 전달되고 전달 받은 함수의 내부에서 어느 특정 시점에 실된다. (T)
- EventTarget.addEventListener(type, listener)에서 type은 이벤트의 종류를 의미하고 listener는 이벤트가 발생을 때, 알림을 받는 객체다.  (T)
-  js에서 함수는 변수에 담을 수 있고, 인자로 전달 할 수 있다. 하지만 반값으로 전달 할 수는 없다. (F)

##### 4. DOM Event에는 다양한 카테고리의 Event들이 존재한다. 아래 제시된 Event들이 각각 어떤 시점에 발생하는지 간단하게 작성하시오. 참고 

- click -  마우스로 클릭했을때

- mouseover - 포인팅 장치가 리스너가 등록된 엘리먼트나 그 자식 엘리먼트의 위로 이동했을 때.

- mouseout - 포인팅 장치가 리스너가 등록된 엘리먼트 또는 그 자식 엘리먼트의 밖으로 이동했을 때.

- keypress - 쉬프트, Fn, CapsLock 을 제외한 키가 눌린 상태일 때(연속적으로 실행됨.).

- keydown - 키가 눌렸을 때 (누르고 있을때 한번만 실행)

- keyup - 키 누름이 해제될 때

- load - 리소스와 그 의존 리소스의 로딩이 끝났을 때.

- scroll - 다큐먼트 뷰나 엘리먼트가 스크롤되었을 때.

- change - 폼 컨트롤(value의 값)의 `값이 변경 되었을 때 발생하는 이벤트다.

  