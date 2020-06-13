<template>
  <div class="pt-3 px-5 mb-2 bg-light text-dark">

    <div>
      <div class="text-right">
        <label for="rank">평점 : </label>
        <input if="rank" type="number" min="0" max="10" v-model="rankData.rank"/><br>

        
      </div>
      <div>
        <div class="input-group">
          <div class="input-group-prepend">
            <span class="input-group-text">한줄평</span>
          </div>
          <textarea class="form-control" id="content" aria-label="With textarea" v-model="rankData.content"></textarea>
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