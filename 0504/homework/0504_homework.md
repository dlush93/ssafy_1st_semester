# 0504_homework

#### 1.  Django는 MTV로 이루어진 Web Framework다. MTV가 무엇의 약자이며 Django에서 각각 어떤 역할을 하고 있는지 작성하시오.

- Model(모델): 모델은 클래스를 나타내며, DB에 저장하는 역할을 한다.
- Template(템플릿): 템플릿은 사용자에게 보여주는 화면을 HTML 파일을 보내준다.
- View(뷰): 뷰는 url에 해당되는 함수를 실행해서, 템플릿에 연결해주는 역할을 한다.





#### 2. 기본적으로 ‘/ ’ 페이지에 접속하게 되면 아래 사진처럼 Page not found 에러가 발생한 다. ‘/ ’ 페이지에 접속했을 때 index.html를 렌더링 하고자 한다. 아래 빈칸에 알맞은 코드를 작성하시오. (프로젝트의 이름은 crud 이며 app 이름은 articles이다. index.html 파일을 렌더링 하는 함수의 이름은 index라고 가정한다.)

- (a):`articles`
- (b):`views`
- (c):`views.index`





##### 3. Django 프로젝트는 기본적으로 render 할 html과 같은 template 파일과 css, js와 같은 static 파일을 앱 폴더 내부의 templates와 static 이름의 폴더에서 찾는다. 만약 해당 위치가 아닌 임의의 위치에 파일을 위치 시키고 싶으면 __(a)__ 파일의 __(b)__과 __(c)__ 이라는 변수에 담긴 리스트의 요소를 수정하면 된다. 빈칸 (a), (b), (c)에 들어갈 내용을 작성하시오.

- (a):`settings.py`
- (b):`TEMPLATES`
- (c):`STATICFILES_DIRS`





##### 4. 아래는 그림과 같이 Django에서 선언한 Model을 Database에 반영하는 과정에서 사용하는 명령어에 대한 설명이다. 각 설명에 해당하는 명령어를 작성하시오.

- `makemigrations Post`
- `showmigrations Post`
- `sqlmigrate Post 0001`
- `migrate Post`



##### 5. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- F
- T
- F
- T



##### 6. 사용자가 업로드한 파일이 저장되는 위치를 Django 프로젝트 폴더(crud) 내부의 /uploaded_files로 지정하고자 한다. 이 때, settings.py에 작성해야 하는 설정 2가지를 작성하시오.

- `MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaded_files')`
- `MEDIA_URL='/uploaded_files/'`



##### 7.  아래의 설명을 읽고 T/F 여부를 작성하시오.

- T
- F
- T
- T
- False





##### 8. 게시글과 댓글의 관계에서 댓글이 존재하는 게시글은 삭제할 수 없도록 __(a)__에 들어갈 코드를 작성하시오. 그리고 이러한 설정이 되어있는 상황에서 Article 객체를 삭제하려고 할 때 발생하는 오류를 작성하시오.

- (a):`PROTECT`
- `ProtectedError`가 발생한다.





##### 9.  Board 모델과 User 모델을 M:N 관계로 설정하여 ‘좋아요’ 기능을 구현하려고 한다. __(a)__와 __(b)__에 들어갈 내용을 작성하시오. 추가적으로 아래의 상황에서 __(b)__를 반드시 작성 해야 하는 이유를 함께 작성하시오.



- (a):`ManyToManyField`
- (b):`related_name`
- 위에 `user`라는 변수로 1:N  관계를 가지고 있기 때문에 `related_name`을 설정안해주면, 역참조시 겹치는 문제가 발생한다.





##### 10.  follow 기능을 구현하기 위해 accounts app의 models.py에 아래와 같은 모델을 작성하였다. Migration 작업 이후에 Database에 만들어지는 테이블의 이름을 작성하고 follow와 관련된 모델의 필드 이름을 각각 작성하시오.



- `accounts_user_followers`
- `from_user_id`
- `to_user_id`