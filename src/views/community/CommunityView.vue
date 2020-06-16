<template>
  <div class="bg-light text-dark w-100 h-100 m-0" style="height:100rm;">

    <div class="d-flex justify-content-center">
      <h1>{{ community.name }}</h1>
      <button data-toggle="modal" :data-target="'#Modal'" class="btn btn-outline-primary justify-content-end">글쓰기</button>
    </div>
    
    <ArticleCreateModal :communityid="community.id" @createArticle="getArticles(community.id)"/>

    <div class="container">
      <div class="row">
        <div class="MenuLeft col-2">
          <p class="mb-4 text-light menu text-center p-1" >커뮤니티 게시판</p>
          <ul class="px-4">
            <!-- <router-link v-for="community in communityList" :key="community.id" :to="`/community/${community.id}`" class="menu-item">{{ community.name }}</router-link> -->
            <li v-for="community in communityList" :key="community.id" class="menu-item" @click="setCommnuity(community)">{{ community.name }}</li>
          </ul>
        </div>

        <div class="px-5 col-10">
          <router-view :articles="articles"></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ArticleCreateModal from '@/components/communitys/ArticleCreateModal.vue'
import Axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/api/v1/community/'

export default {
  name: 'CommunityView',
  data() {
    return {
      articles: null,
      community: {
        name: '등업게시판',
        id: 1
      },
      communityList: [],
    }
  },
  components: {
    ArticleCreateModal,
  },
  methods: {
    getCommunityList() {
      Axios.get(API_URL)
        .then((res)=>{
          this.communityList = res.data
        })
    },
    getArticles(id) {
      Axios.get(API_URL+id)
        .then((res)=>{
          this.articles = res.data
        })
    },
    setCommnuity(community) {
      this.$router.push({ path:'/community', params: {community}},this.test,this.test)
      this.community = community
      this.getArticles(this.community.id)
    },
    test() {
      console.log('!!')
    }
  },
  created() {
    this.getCommunityList()
    this.getArticles(this.community.id)
  },
  updata() {
    this.getArticles(this.community.id)
  },
}

</script>

<style>
  .menu {
    padding-left: 20px;
    background: #163c53;
    color: #fff;
    border-top: 2px solid #008db3;
  }
  .MenuLeft {
    height: 540px;
    background: #10232c;
    padding: 0;
    padding-bottom: 370px;
  }
  .menu-item {
    display: block;
    padding: 0px 0px 0px 10px;
    color: #7a96a7;
    border-bottom: 1px solid #384a56;
    line-height: 30px;
    list-style-type: none;
  }
</style> 