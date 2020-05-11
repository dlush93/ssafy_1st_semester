# 0511_homework

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오



- URI는 정보의 자원 뿐만 아니라 HTTP Method를 통해 무엇을 어떻게 하고 싶은지 명확하게 나타내야 한다.  (F)
- 자원에 대한 행위는 HTTP Method로 표현한다.  (T)
- 일반적으로 주소 마지막에 슬래시( / )는 포함하지 않는다. (T)
- https://www.fifa.com/worldcup/teams/team/43822/create/는 계층 관계를 잘 표현한 RESTful한 URI라고 할 수 있다(F)





### 2.  다음의 HTTP status code의 의미를 간략하게 작성하시오. 

- 200 : OK
  - 요청이 성공적으로 되었습니다. 성공의 의미는 HTTP 메소드에 따라 달라집니다:
    GET: 리소스를 불러와서 메시지 바디에 전송되었습니다.
    HEAD: 개체 해더가 메시지 바디에 있습니다.
    PUT 또는 POST: 수행 결과에 대한 리소스가 메시지 바디에 전송되었습니다.
    TRACE: 메시지 바디는 서버에서 수신한 요청 메시지를 포함하고 있습니다.
- 400 : BAD Request
  - 이 응답은 잘못된 문법으로 인하여 서버가 요청을 이해할 수 없음을 의미합니다.
- 401 : Unauthorized
  - 비록 HTTP 표준에서는 "미승인(unauthorized)"를 명확히 하고 있지만, 의미상 이 응답은 "비인증(unauthenticated)"을 의미합니다. 클라이언트는 요청한 응답을 받기 위해서는 반드시 스스로를 인증해야 합니다.
- 403 : Forbidden
  - 클라이언트는 콘텐츠에 접근할 권리를 가지고 있지 않습니다. 예를들어 그들은 미승인이어서 서버는 거절을 위한 적절한 응답을 보냅니다. 401과 다른 점은 서버가 클라이언트가 누구인지 알고 있습니다.
- 404 : Not Found
  - 서버는 요청받은 리소스를 찾을 수 없습니다. 브라우저에서는 알려지지 않은 URL을 의미합니다. 이것은 API에서 종점은 적절하지만 리소스 자체는 존재하지 않음을 의미할 수도 있습니다. 서버들은 인증받지 않은 클라이언트로부터 리소스를 숨기기 위하여 이 응답을 403 대신에 전송할 수도 있습니다. 이 응답 코드는 웹에서 반복적으로 발생하기 때문에 가장 유명할지도 모릅니다.
- 500 : Internal Server Error
  - 서버가 처리 방법을 모르는 상황과 마주쳤다. 서버는 아직 처리 방법을 알 수 없다.





### 3. DRF를 활용하여 학생 정보를 제공하는 API를 제작하고자 한다. 학생 모델은 models.py에 아래와 같이 정의되어 있고, 학생 모델의 데이터를 다른 유형의 데이터 포맷으로 변환할 수 있는 Serializer를 정의하려고 한다. Serializers.py 파일에 들어갈 StudentSerializer를 정의하시오. 단, name과 address 필드는 반드시 포함되어야 한다.

```python
from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','address']

```

