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
        <UserLikeArticleListitem :article="article"  v-for="article in likeArticleList" :key="article.id" />
      </tbody>
    </table>
  </div>
</template>

<script>
import UserLikeArticleListitem from '@/components/profile/UserLikeArticleListitem.vue'
import axios from 'axios'
const BASE_URL = 'http://127.0.0.1:8000/'
const API_URL = BASE_URL+'accounts/like_article/'
export default {
  name : 'UserLikeArticleList',
  data(){
    return {
      likeArticleList : [],
    }
  },
  components : {
    UserLikeArticleListitem
  },
  methods: {
    Likearticleget(){
      const username = this.$route.params.username
      axios.get(API_URL+username)
      .then((res)=>{
        console.log(res.data,'얍')
        this.likeArticleList = res.data
      })
    }
  },
  created(){
    this.Likearticleget()
  }
}
</script>

<style scoped>
th {
  color: white;
}

</style>