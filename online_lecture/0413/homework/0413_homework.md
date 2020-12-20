## 0413_homework

### 1. django에서 기본적으로 사용하는 User 모델은 다음과 같은 경로에서 찾아볼 수 있다. 아래의 Django 공식 저장소에서 User 모델이 정의된 코드를 찾아 작성하시오. 

```python
class User(AbstractUser):

    """

    Users within the Django authentication system are represented by this

    model.



    Username and password are required. Other fields are optional.

    """

    class Meta(AbstractUser.Meta):

        swappable = 'AUTH_USER_MODEL'
```



### 2. 기본 User 모델의 정보를 생성하기 위하여 Django 내부에 정의된 ModelForm을 불러오는 import 문장을 작성하시오.

```python
from django.contrib.auth.forms import UserCreationForm
```



### 3.  views.py에 정의된 함수를 post 요청에 대해서만 실행하게 하기 위하여 추가하는 require_POST 함수를 불러오는 import 문장을 작성하시오.

```python
from django.views.decorators.http import require_POST
```

