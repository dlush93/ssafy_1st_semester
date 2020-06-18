<template>
  <div>
    <table class="table mt-5">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">작성 게시판</th>
          <th scope="col">제목</th>
          <th scope="col">작성 시간</th>
        </tr>
      </thead>
      <tbody>
        <UserArticleListitem :article="article"  v-for="article in articleList" :key="article.id" />
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
import UserArticleListitem from '@/components/profile/UserArticleListitem.vue'
const API_URL = 'http://127.0.0.1:8000/accounts/articles/'
export default {
  name : 'UserArticleList',
  data(){
    return {
      articleList : []
    }
  },
  components : {
    UserArticleListitem,
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

<style scoped>
th {
  color: white;
}

</style>