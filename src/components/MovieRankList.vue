<template>
  <div class="p-3 mb-2 bg-light text-dark">
    <h1>ArticleList</h1>

    <label for="content">내용</label>
    <input id="content" type="text" v-model="rankData.content">
    <label for="rank">평점</label>
    <input if="rank" type="number" min="0" max="10" v-model="rankData.rank"/>
    <button @click="createRank">작성</button>
    <p class="text-left">댓글 {{ movie.movierank_count }}개</p>
    <MovieRankListItem v-for="movierank in movie.movierank" :key="movierank.id"/>
  </div>
</template>

<script>
import MovieRankListItem from '@/components/MovieRankListItem.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/api/v1/movies/'
// <int : movie.id>/comments
export default {
  name: 'MovieRankList',
  data() {
    return {
      rankData: {
        'content': '',
        'rank': 5
      }
    }
  },
  props: {
    movie: {
      type: Object
    },
  },
  components: {
    MovieRankListItem
  },
  methods: {
    createRank() {
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(API_URL + this.movie.id + '/comments/', this.rankData, request_header)
        .then((res)=>{
          console.log(res)
          console.log(this.movie.id)

          // 현재 새로고침
          this.$router.go()
        })
        .catch((err)=>{
          console.log(err.response)
        })
    },
  },
}
</script>

<style>

</style>