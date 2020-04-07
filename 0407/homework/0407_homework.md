# 0407_homework

### 1.  모델폼을 정의하기 위해 빈칸에 들어갈 코드를 작성하시오

- (a)=`form.ModelForm`
- (b)=`Meta`



### 2. 글 작성 기능을 구현하기 위해 다음과 같이 코드를 작성하였다. 서버를 실행시킨 후 기능을 테스트 해보니 특정 상황에서 문제가 발생하였다. 이유와 해결방법을 작성하시오.

- 만약 `create`에서 사용자가 입력을 해서 제출했는데, 만약 content, title에 입력이 없거나 유효하지 않은 정보가 들어왔을때, return 되는 것이 없어서 오류가 발생된다.
- 그래서 해결 방법은 `else` 밑에 있는 `context` 밑을 넣어쓰기로 해줘서 유효하지 않은 form이 들어왔을때, return이 가능하게 해준다.



### 3. 글 수정 기능을 구현하기 위해 빈칸에 들어갈 코드를 작성하시오.

- (a)  `form=ReservationForm(request.POST,instance=reservation)`
- (b)   `form=ReservationForm(instance=reservation)`



### 4.  글 수정 기능을 구현하기 위해 빈칸에 들어갈 수 있는 코드를 모두 작성하시오.

- (a) `as_table`,`as_p`,`as_ul`