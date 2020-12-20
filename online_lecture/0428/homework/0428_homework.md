# 0428_homework


### 1. 다음 중 맞으면 T, 틀리면 F를 작성하고 틀렸다면 이유를 함께 작성하시오.

1. True
2. True
3. False : related_name은 선택적이다.





### 2. 아래 빈 칸에 들어갈 코드를 각각 작성하시오.

(a)=`user`

(b)=`article.like_user.all`





### 3. 모델 정보가 다음과 같을 때 빈칸에 들어갈 코드를 각각 작성하시오.

(a)=`username`

(b)= `followers`

(c)=`filter`

(d)=`remove`

(e)=`add`





### 4.  아래와 같은 에러 메시지가 발생하는 이유와 이를 해결하기 위한 방법을 작성하시오.

UserCreationForm을 수정 해서 Custom을 만들어줘야한다.





### 5.  아래의 경우 related_name을 필수적으로 설정해야 한다. 그 이유를 설명하시오.



- 기본값으로 설정시 1:N 관계인 user와 M:N 관계인 like_user의 역참조 값이 article_set으로 동일하게 되어, 문제가 발생하게된다.
- 그래서 해결방법은 둘 중 하나의 related_name을 바꿔줘야한다.





### 6. Person에는 view에서 넘어온 유저 정보가 담겨 있고 모델 정보가 아래와 같을 때, 빈칸에 들어갈 코드를 각각 작성하시오.

(a)=`person.followings`

(b)=`person.followers`



(c)=`user`

(d)=`person`

(e)=`person.username`