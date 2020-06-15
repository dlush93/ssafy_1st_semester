<template>
  <div class="pt-3 px-5 mb-2 bg-light text-dark">

    <div>
      <div class="d-flex float-right align-items-center mb-2">
        <span class="mr-2">평점 : {{rank*2}} 점</span>
        <star-rating :increment="0.5" v-model="rank" :star-size="30" :show-rating="false"></star-rating>
      </div>
      <div>
        <div class="input-group">
          <div class="input-group-prepend">
            <span class="input-group-text">한줄평</span>
          </div>
          <textarea class="form-control" id="content" aria-label="With textarea" v-model="content"></textarea>
        </div>
      </div>
      <button @click="createRank" class="btn btn-primary mt-2">작성</button>
    </div>

    <div>
      <div class="d-flex">
        <p class="text-left mb-0">한줄평</p>
        <span class="mx-3"> | </span>
        <p class="mb-0">총 : {{ movie.movierank_count }}개</p>
      </div>
      <hr class="my-1">

      <MovieRankListItem v-for="movierank in movie.movierank" :key="movierank.id" :movierank="movierank"/>
    </div>
  </div>
</template>

<script>
import MovieRankListItem from '@/components/movies/MovieRankListItem.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/api/v1/movies/'
// <int : movie.id>/comments
export default {
  name: 'MovieRankList',
  data() {
    return {
      rating: null,
      rank: 3,
      content: ''
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
      if(!this.$cookies.isKey('auth-token')) {
        this.$router.push({ name: 'Login'})
      }
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(API_URL + this.movie.id + '/comments/', {rank: this.rank*2, content: this.content}, request_header)
        .then(()=>{
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