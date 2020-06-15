<template>
  <div class="bg-light text-dark w-100 h-100 m-0" style="height:100rm;">

    <div>
      <h1>Community Detail</h1>
    </div>

    <div class="container">
      <div class="row">
        <div class="MenuLeft col-2">
          <p class="mb-4 text-light menu text-center p-1" >커뮤니티 게시판</p>
          <ul class="px-4">
            <li v-for="community in communityList" :key="community.id" class="menu-item" @click="setCommnuity(community.id)">{{ community.name }}</li>
          </ul>
        </div>
        <div class="px-5 col-10">
          <ArticleDetail />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ArticleDetail from '@/components/communitys/ArticleDetail.vue'
import Axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/api/v1/community/'

export default {
  name: 'CommunityDetailView',
  components: {
    ArticleDetail
  },
  data() {
    return {
      article: null,
      communityList: [],
    }
  },
  methods: {
    getCommunityList() {
      Axios.get(API_URL)
        .then((res)=>{
          this.communityList = res.data
        })
    },
    getArticle(id) {
      Axios.get(API_URL)
        .then((res)=>{
          console.log(res.data)
          console.log(id)
          
        })
    }
  },
  created() {
    this.getCommunityList()
    // this.getArticle(this.communityid)
  },
}
</script>

<style>

</style>