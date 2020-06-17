<template>
  <div class="container">
    <div class="row">
      <div class="col-12 border border-light mb-5" style="height:25vh;">
        <div class="row">
          <div class="col-12 border border-light" style="color:white; height:5vh">
            {{username}}님의 활동내역
          </div>
          <div class="col-12">
            <div class="row">
              <div class="col-2" style="border-right:1px solid white;">
                <div class="row">
                  <div class="col-12 my-auto"  style="height:10vh; border-bottom: 1px solid white;line-height: 10vh">
                    회원등급
                  </div>
                  <div class="col-12" style="height:10vh;line-height: 10vh">
                    {{user.grade}}
                  </div>
                </div>
              </div>
              <div class="col-10">
                <div class="row">
                  <div class="col-4 py-1" style="height:10vh">
                    <div class="row">
                      <div class="col-12">작성글 수</div>
                      <div class="col-12 py-1">{{user.article_count}}</div>
                    </div>
                  </div>
                  <div class="col-4 py-1">
                    <div class="row">
                      <div class="col-12">작성댓글 수</div>
                      <div class="col-12 py-1">{{user.comment_count}}</div>
                    </div>
                  </div>
                  <div class="col-4 py-1">
                    <div class="row">
                      <div class="col-12">받은 좋아요 수</div>
                      <div class="col-12 py-1">{{user.received_count}}</div>
                    </div>
                  </div>
                  <div class="col-6">
                    <div class="row">
                      <div class="col-12">평점을 단 영화 수</div>
                      <div class="col-12 py-1">{{user.rank_count}}</div>
                    </div>
                  </div>
                  <div class="col-6">
                    <div class="row">
                      <div class="col-12">내가 좋아요를 준 글수</div>
                      <div class="col-12 py-1">{{user.like_count}}</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
    <svg id="articlesrc" xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="gray" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-book"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg><router-link :to="`/accounts/${username}/article/`">작성글 보기</router-link> |
    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="gray" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-thumbs-up"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg><router-link :to="`/accounts/${username}/likearticle/`">좋아요 한글 보기</router-link> |
    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="gray" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg><router-link :to="`/accounts/${username}/rankedmovie/`">평점 단 영화 보기</router-link>
    <router-view></router-view>

  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000/accounts/profile/'
export default {
  name: 'UserProfileView',
  data(){
    return {
      username : null,
      user : []
   }
    },
  methods : {
    routerCheck(){
      this.username = this.$route.params.username
    },
    profilecheck(){
      axios.get(API_URL+this.username)
      .then(res=>{
        this.user = res.data
      })
    }
  },
  created(){
    this.routerCheck()
    this.profilecheck()
  },
 

}
</script>

<style>

</style>