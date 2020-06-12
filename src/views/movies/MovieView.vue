<template>
  <div class="col-12">
    <h1>Movie View</h1>
    <MovieList :movies='movies'/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/api/v1/movies/'

export default {
  name: 'MovieView',
  components: {
    MovieList,
  },
  data() {
    return {
      movies: null
    }
  },
  methods: {
    GetMovie() {
      axios.get(API_URL)
        .then((res)=>{
          this.movies = res.data.results
        })
    }
  },
  created() {
    this.GetMovie()
  }
}
</script>

<style>

</style>