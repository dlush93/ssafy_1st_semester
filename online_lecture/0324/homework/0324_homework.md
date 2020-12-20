### 1. 상단 코드의 bootstrap grid system을 적용시키고자 할때, {a},{b} 각각에 입력해야할 클래스 이름을 작성하시오.

- {a}=`container`
- {b}=`row`

### 2. Bootstrap Grid system에서 요소의 크기를 지정하기 위해서는 상단 코드와 같은 형태로 클래스 이름을 지정해야 한다.

- {c}에 들어 갈수 있는 값과 그 값들이 가지는 의미를 작성하시오.
  - {c} = `break point`  지정된 사이즈이상에서 적용 될수 있는 크기를 결정해주는 역할로서,

    - `sm`은 576px 이상

    - `md`은 768px 이상

    - `lg`은 992px 이상

    - `xl`은 1200px 이상

      에서만 적용되는 line width을 결정지어주는 역할을 해야한다.

- {d}에 들어갈 수 있는 값과 그 값들이 가지는 의미를 작성하시오.
  - {d} =`line width`  한 줄을 12칸으로 지정하여, 0이상 12이하의 정수를 넣어, 해당 div의 line width을 결정해준다.

### 3. Align-items-center를 사용하려면 `d-flex` 클래스와 함께 사용하여야 했었다. 그러나, Grid System 에서는 `d-flex` 클래스를 생략하여도 올바르게 동작한다. 그 이유를 작성하시오.

- bootstrap에 정의된 `row`에 `display:flex` 라고 이미 정의되어 있어서 가능하다.

### 4. Nav를 그림과 같이 오른쪽 정렬 하고자 할 때 {a}에 들어가야 할 클래스 이름을 작성하시오.

- `justify-content-end` 이다. `d-flex`를 지정하지 않아도 `nav` 클래스 내에 `display:flex`가 정의되어 있다.

