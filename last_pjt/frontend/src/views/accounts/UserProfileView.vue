<template>
  <div>
    <router-link :to="`/accounts/${username}/article/`">작성글 보기</router-link> |
    <router-link :to="`/accounts/${username}/article/`">좋아요 한글 보기</router-link> |
    <router-link :to="`/accounts/${username}/article/`">평점 단 영화 보기</router-link>
    <h1>{{username}}</h1>
    <router-view></router-view>

  </div>
</template>

<script>
export default {
  name: 'UserProfileView',
  data(){
    return {
      username : null
   }
    },
  methods : {
    routerCheck(){
      this.username = this.$route.params.username
    },
  },
  created(){
    this.routerCheck()
  },
 

}
</script>

<style>

</style>