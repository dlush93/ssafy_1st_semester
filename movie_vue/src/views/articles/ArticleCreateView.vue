<template>
  <div class="col-6">
    <h1>커뮤니티</h1>
    <div class="form-group">
      <label for="InputTitle">Title</label>
      <input type="text" class="form-control" id="InputTitle" aria-describedby="InputTitle" v-model="articleData.title">
      <small id="InputTitle" class="form-text text-muted">영화와 관련된 자유로운 의견을 남겨주세요.</small>
    </div>
    <div class="form-group">
      <label for="InputContent">Content</label>
      <textarea name="content"  cols="30" rows="5" class="form-control" id="InputContent" aria-describedby="InputContent" v-model="articleData.content" placeholder="추천 바합니다"></textarea>
    </div>
    <button type="submit" class="btn btn-primary" @click="write">작성하기</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleCreateView',
  data() {
    return {
      articleData: {
        title: null,
        content: null,
      }
    }
  },
  methods: {
    write(){
      const requestHeader = {
        headers :{
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${API_URL}/articles/create/`, this.articleData, requestHeader)
        .then(res=>{
          console.log(res)
          this.$router.push('/')
        })
        .catch(err=>{
          console.log(err.response)
        })

    }
  }
}
</script>

<style>

</style>