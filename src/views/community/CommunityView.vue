<template>
  <div class="bg-light text-dark w-100 h-100 m-0" style="height:100rm;">

    <div>
      <h1>Community</h1>
      <button data-toggle="modal" :data-target="'#Modal'">글쓰기</button>
    </div>
    
    <ArticleCreateModal :communityid="communityid" @createArticle="getArticles(communityid)"/>

    <div class="container">
      <div class="row">
        <div class="MenuLeft col-2">
          <p class="mb-4 text-light menu text-center p-1" >커뮤니티 게시판</p>
          <ul class="px-4">
            <li v-for="community in communityList" :key="community.id" class="menu-item" @click="setCommnuity(community.id)">{{ community.name }}</li>
          </ul>
        </div>

        <div class="px-5 col-10">
          <ArticleList :articles="articles"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ArticleCreateModal from '@/components/communitys/ArticleCreateModal.vue'
import ArticleList from '@/components/communitys/ArticleList.vue'
import Axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/api/v1/community/'

export default {
  name: 'CommunityView',
  data() {
    return {
      articles: null,
      communityid: 1,
      communityList: [],
    }
  },
  components: {
    ArticleCreateModal,
    ArticleList,
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
    setCommnuity(id) {
      this.communityid = id
      this.getArticles(this.communityid)
    },
  },
  created() {
    this.getCommunityList()
    this.getArticles(this.communityid)
  },
  updata() {
    this.getArticles(this.communityid)
  }
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
    padding: 0px 0px 0px 10px;
    color: #7a96a7;
    border-bottom: 1px solid #384a56;
    line-height: 30px;
    list-style-type: none;
  }
</style> 