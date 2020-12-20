# 0420_workshop

### 1. countries 테이블을 생성하시오.

```sql
sqlite> CREATE TABLE countries(
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> room_num TEXT NOT NULL,
   ...> check_in TEXT NOT NULL,
   ...> check_out TEXT NOT NULL,
   ...> grade TEXT NOT NULL,
   ...> price INTEGER NOT NULL
   ...> );
```

### 2. 데이터를 입력하시오.

```sql
sqlite> INSERT INTO countries
   ...> VALUES(1,'B203','2019-12-31','2020-01-03','suite',900);
sqlite> INSERT INTO countries
   ...> VALUES(2,'1102','2020-01-04','2020-01-08','suite',850);
sqlite> INSERT INTO countries
   ...> VALUES(3,'303','2020-01-01','2020-01-03','deluxe',500);
sqlite> INSERT INTO countries
   ...> VALUES(4,'807','2020-01-04','2020-01-07','superior',300);
```

### 3. 테이블의 이름을 hotels로 변경하시오.

```sql
ALTER TABLE countries RENAME TO hotels;
sqlite> .table
hotels
```

### 4. 객실 가격을 내림차순으로 정렬하여 상위 2개의 room_num와 price를 조회하시오.

```sql
SELECT room_num,price FROM hotels
ORDER by price DESC
LIMIT 2;

room_num | price
B203 | 900
1102 | 850
```

### 5. grade 별로 분류하고 분류된 grade 개수를 내림차순으로 조회하시오.

```sql
SELECT grade,COUNT(grade) FROM hotels
GROUP BY grade
ORDER by COUNT(grade) DESC;



grade | COUNT(grade)
suite | 2
deluxe | 1
superior | 1
```

### 6. 객실의 위치가 지하 혹은 등급이 deluxe인 객실의 모든 정보를 조회하시오.

```sql
SELECT * FROM hotels
WHERE room_num LIKE 'B%' OR grade='deluxe';

id | room_num | check_in | check_out | grade | price
1 | B203 | 2019-12-31 | 2020-01-03 | suite | 900
3 | 303 | 2020-01-01 | 2020-01-03 | deluxe | 500
```



### 7. 지상층 객실이면서 2020년 1월 4일에 체크인 한 객실의 목록을 price 오름차순으로 조회하시오.

```sql
SELECT * FROM hotels
WHERE room_num NOT LIKE 'B%' AND check_in='2020-01-04'
ORDER by price ASC;

id | room_num | check_in | check_out | grade | price
4 | 807 | 2020-01-04 | 2020-01-07 | superior | 300
2 | 1102 | 2020-01-04 | 2020-01-08 | suite | 850
```

