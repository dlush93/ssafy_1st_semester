<template>
  <div class="col-10">
    <div class="jumbotron">
      <h1 class="display-4 mb-5"> {{ article.title }} </h1>
      <p class="lead text-left">내 용 : {{ article.content }}</p>
      <hr class="my-4 ">
      <p class="text-left">작성자 : {{ article.user.username }}</p>
      <p class="text-left">수정일 : {{ article.created_at }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetailView',
  data() {
    return {
      article_pk: this.$route.params.id,
      article: {
        title: null,
        content: null,
        user: {
          username: null
        },
        created_at: null
      }
    }
  },
  methods: {
    loadArticle() {
      axios.get(`${API_URL}/articles/${this.article_pk}`)
        .then((res)=>{
          this.article = res.data
        })
    }
  },
  created() {
    this.loadArticle()
  }
}
</script>

<style>

</style>