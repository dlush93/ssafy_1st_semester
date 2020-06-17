<template>
  <div>
    <div class="row articleHead p-2 text-center mb-3">
      <p class="mb-0">{{ article.user.username }}</p>
      <p class="mx-auto mb-0">{{ article.created_at | moment('YYYY-MM-DD HH:mm') }}</p>
      <p class="mb-0">추천수</p>
    </div>
    <div class="blog-main">
      <div class="blog-post mb-5">
        <h2 class="blog-post-title">{{ article.title }}</h2>
        <hr>
      </div>

      <div class="blog-post">
        <p>{{ article.content}}</p>
        <hr class="mt-3">
      </div>
      
      <nav class="blog-pagination mbt-5">
        <p class="btn btn-outline-primary" @cilck="like"> 추 천 </p>
        <p class="btn btn-outline-secondary disabled"> {{ article.like_users_count }}명</p>
      </nav>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const LIKE_URL = 'http://127.0.0.1:8000/api/v1/community/like/'

export default {
  name: 'ArticleDetail',
  data() {
    return {
      article: this.$route.params.article
    }
  },
  methods: {
    like() {
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`,
        }
      }
      axios.post(LIKE_URL+this.article.id,null,request_header)
        .then((res)=>{
          console.log(res.data)
        })
    }
  },
}
</script>

<style>
</style>