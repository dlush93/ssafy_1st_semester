<template>
  <div class="col-10">
    <router-link to="articles/create" class="btn btn-success mb-5">글쓰기</router-link>
    <h1>게시판</h1>

    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">제목</th>
          <th scope="col">작성자</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="article in articles" :key="article.id">
          <th scope="row">{{ article.id }}</th>
          <td><router-link :to="{ name : 'ArticleDetailView', params: {id: article.id }}">{{ article.title }}</router-link></td>
          <td>{{ article.user.username }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleListView',
  data() {
    return {
      articles: null
    }
  },
  methods: {
    loadArticle() {
      axios.get(`${API_URL}/articles/`)
        .then((res)=>{
          this.articles = res.data
        })
        .catch((err)=>{
          console.log(err.response)
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