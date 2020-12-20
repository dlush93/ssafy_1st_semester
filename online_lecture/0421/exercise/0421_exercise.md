# 0421_exercise

### 1.  user 테이블 전체 데이터를 조회하시오

```python
User.objects.all()
```

### 2.  id가 19인 사람의 age를 조회하시오.

```python
User.objects.get(id=19).age
```

### 3. 모든 사람의 age를 조회하시오.

```python
users=User.objects.all()
users.values('age') 

-----
 User.objects.all().values('age')
```

### 4. age가 40 이하인 사림들의 id와 balance를 조회하시오.

```python
User.objects.filter(age__lte=40)
    ...: .values('id','balance') 
<QuerySet [{'id': 1, 'balance': 370}, {'id': 2, 'balance': 5900}, {'id': 3, 'balance': 3100}, {'id': 4, 'balance': 250000}, {'id': 5, 'balance': 220}, {'id': 6, 'balance': 530}, {'id': 7, 'balance': 390}, {'id': 8, 'balance': 3700}, {'id': 9, 'balance': 43000}, {'id': 10, 'balance': 49000}, {'id': 11, 'balance': 640000}, {'id': 12, 'balance': 52000}, {'id': 13, 'balance': 35000}, {'id': 14, 'balance': 720}, {'id': 15, 'balance': 35000}, {'id': 16, 'balance': 720}, {'id': 17, 'balance': 440}, {'id': 18, 'balance': 94000}, {'id': 19, 'balance': 6100}, {'id': 20, 'balance': 590}, '...(remaining elements truncated)...']>
```

### 5.  last_name이 ‘김’이고 balance가 500 이상인 사람들의 first_name을 조회하시오.

```python
User.objects.filter(last_name='김',balance__gte=500).values('first_name')   
```



### 6.  first_name이 ‘수’로 끝나면서 행정구역이 경기도인 사람들의 balance를 조회하시오.

```python
User.objects.filter(first_name__endswith='수',country='경기도').values('balance')
```



### 7.  balance가 2000 이상이거나 age가 40 이하인 사람의 총 인원수를 구하시오.

```python
from django.db.models import Q
User.objects.filter(Q(balance__gte='2000')|Q(age__lte=40)).count()
```

### 8. phone 앞자리가 ‘010’으로 시작하는 사람의 총원을 구하시오.

```python
User.objects.filter(phone__startswith='010').count()
```

### 9.이름이 ‘김옥자’인 사람의 행정구역을 경기도로 수정하시오.

```python
User.objects.get(first_name='옥자',last_name='김').update(country='경기도')


user=User.objects.get(first_name='옥자',last_name='김')
user.country='경기도'
user.save()	
```

### 10. 이름이 ‘백진호’인 사람을 삭제하시오.

```python
user=User.objects.get(first_name='진호',last_name='백')
user.delete()
```

### 11.  balance를 기준으로 상위 4명의 first_name, last_name, balance를 조회하시오.

```python
User.objects.order_by('-balance').values('first_name','last_name')[:4]
```



### 12. phone에 ‘123’을 포함하고 age가 30미만인 정보를 조회하시오.

```python
User.objects.filter(phone__contains=123,age__lt=30)
```

### 13.  phone이 ‘010’으로 시작하는 사람들의 행정 구역을 중복 없이 조회하시오.

```python
User.objects.filter(phone__startswith='010').values('country').distinct()
```

### 14. 모든 인원의 평균 age를 구하시오.

```python
User.objects.aggregate(Avg('age'))
```

### 15. 박씨의 평균 balance를 구하시오.

```python
User.objects.filter(last_name='박').aggregate(Avg('balance'))
```

### 16. 경상북도에 사는 사람 중 가장 많은 balance의 액수를 구하시오.

```py
User.objects.filter(country='경상북도').aggregate(Max('balance'))
```

### 17. 제주특별자치도에 사는 사람 중 balance가 가장 많은 사람의 first_name을 구하시오.

```python
User.objects.filter(country='제주특별자치도').order_by('-balance')[0].first_name
User.objects.filter(country='제주특별자치도').aggregate(Max('balance')).values('first_name')
```

