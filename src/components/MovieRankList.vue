<template>
  <div class="p-3 mb-2 bg-light text-dark">
    <h1>ArticleList</h1>
    <input type="text" v-model="input">
    
    <div class="wrap-star">
      <div class='star-rating'>
        <span style ="width:30%"></span>
      </div>
    </div>
    <button>작성</button>
    <p class="text-left">댓글 {{ movie.movierank_count }}개</p>
    <MovieRankListItem v-for="movierank in movie.movierank" :key="movierank.id"/>
  </div>
</template>

<script>
import MovieRankListItem from '@/components/MovieRankListItem.vue'
import axios from 'axios'

// const API_URL = 'http://127.0.0.1:8000/api/v1/movies/'
// <int : movie.id>/comments
export default {
  name: 'MovieRankList',
  data() {
    return {
      input: '',
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
      axios.post()
    }
  }
}
</script>

<style>
  .star-rating { width:205px; }
  .star-rating,.star-rating span { display:inline-block; height:39px; overflow:hidden; background: url('../assets/star.png') no-repeat; }
  .star-rating span{ background-position:left bottom; line-height:0; vertical-align:top; }
</style>