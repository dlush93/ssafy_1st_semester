# 0519_workshop

```html
{% extends 'base.html' %}

{% block content %}
  <h2>INDEX</h2>
  {% for article in articles %}
    <h3>작성자: {{ article.user }}</h3>
    <h4>제목: {{ article.title }}</h4>
    <p>내용: {{ article.content }}</p>

    {% if user in article.like_users.all %}
      <i class="fas fa-heart fa-lg" style="color:crimson" data-id = "{{article.id}}">♥</i>
    {% else %}
      <i class="fas fa-heart fa-lg" style="color:black" data-id = "{{article.id}}">♡</i>
    {% endif %}
    <span><span id = "like-count-{{article.id}}">{{ article.like_users.all|length }}</span> 명이 이 글을 좋아합니다.</span>
    <hr>
  {% endfor %}
  <a href="{% url 'articles:create' %}">CREATE</a>


  <!-- 좋아요 기능 ajax로 처리하기 위해서 작성하는 js -->
  
  <script>
    const heartBtns = document.querySelectorAll('i')
    console.log(heartBtns)

    heartBtns.forEach((heartBtn)=>{
      heartBtn.addEventListener('click',function (event){
        const articleId = event.target.dataset.id

        const countSpan = document.querySelector(`#like-count-${articleId}`)

        axios.get(`/articles/${articleId}/like/`)
        .then((response)=>{
          if (response.data.status) {
            event.target.style.color = "crimson"
            event.target.innerText = '♥'
            countSpan.innerHTML = response.data.count

          }
          else {
            event.target.style.color = "black"
            event.target.innerText = '♡'
            countSpan.innerHTML = response.data.count
          }
          
          
        })
      })
    })

  </script>


{% endblock %}

```

