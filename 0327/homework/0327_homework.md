### 1. Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무 엇의 약자이며 각각 MVC 디자인 패턴과 어떻게 매칭이 되는지 작성하시오.

- Model template view
- Model->Model
- template->view
- view->controller

###  2. ____(a)____는 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것 을 의미한다. (a)는 무엇인지 작성하시오.

-  variable routing



### 3.  Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에 등록된 각 앱 폴더 안의 (a) 폴더 내부를 탐색한다. (a)에 들어갈 폴더 이름을 작성하 시오.

- templates

### 4. Static web page와 Dynamic web page의 특징을 간단하게 서술하시오.

- Static web page의 특징
  - 서버에 미리 저장된 파일이 그대로 전달되는 웹페이지
  - 서버는 사용자가 요청에 해당되는 저장된 웹페이지를 보냄
  - 사용자는 서버에 저장된 데이터가 변경되지 않는 한 고정된 웹페이지를 보게됨
- Dynamic web page의 특징
  - 서버에 있는 데이터들을 스크립트에 의해 가공처리한 후 생성되어 전달되는 웹페이지
  - 서버는 사용자의 요청을 해석하여 데이터를 가공한 후 생성되는 웹페이지를 보냄
  - 사용자는 상황,시간,요청 등에 따라 달라지는 웹페이지를 보게 됨