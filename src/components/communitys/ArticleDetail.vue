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
        <p v-html="article.content"></p>
        <hr class="mt-3">
      </div>
      
      <nav class="blog-pagination mbt-5">
        <button class="btn btn-outline-primary" :class="{likestatus: this.likestatus}" @click="like"> 추 천 </button>
        <p class="btn btn-outline-secondary disabled m-0"> {{ article.like_users_count }}명</p>
      </nav>

      <div v-if="'admin'===username" >
          <button class="btn btn-outline-primary" @click="gradeup">등업 시키기</button>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'

const LIKE_URL = 'http://127.0.0.1:8000/api/v1/community/like/'
const USER_URL = 'http://127.0.0.1:8000/accounts/'

export default {
  name: 'ArticleDetail',
  data() {
    return {
      article: this.$route.params.article,
      likestatus : false,
      username: '',
    }
  },
  props :{
    community : {
      type : Object
    }
  },
  methods: {
    getUser() {
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`,
        }
      }
      axios.post(USER_URL,null,request_header)
        .then((res)=>{
          this.username = res.data.username
        })
    },
    like() {
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`,
        }
      }
      axios.post(LIKE_URL+this.article.id,null,request_header)
        .then((res)=>{
          this.likestatus = res.data.likestatus
          if (this.likestatus) {
            this.article.like_users_count += 1
          }else {
            this.article.like_users_count -= 1
          }
          alert(res.data.message)
        })
    },
    gradeup(){
      alert("이창완4 회원등급 완료")
    }
  },
  created(){
    this.getUser()
  },
  updated(){
    this.getUser()
  }
}
</script>

<style>
  .likestatus {
    background: red ;
    color: seashell;
    border: red;
  }

</style>