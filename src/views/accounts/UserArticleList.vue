<template>
  <div>
    <h1>이건 작성글 페이집니다.</h1>
    
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000/accounts/articles/'
export default {
  name : 'UserArticleList',
  data(){
    return {
      articleList : []
    }
  },
  methods:{
    check(){
      const username = this.$route.params.username
      axios.get(API_URL+username)
      .then((res)=>{
        this.articleList = res.data
      })
    }
  },
  created(){
    this.check()
  }
}
</script>

<style>

</style>