<template>
  <div class="col-12">
    <div style="height: 100vh">
      <img src="https://image.tmdb.org/t/p/w342//tlJuznSuaX4XsRsZ7l7RTHYAwEr.jpg" style="height: 50vh" alt="">
      <div style="height: 50vh">
        <h1 class="mt-5">추천영화</h1>
        <MovieList :movies='movies'/>
      </div>
    </div>
    <h1>장르</h1>
    <MovieList :movies='movies'/>
    <h1>장르</h1>
    <MovieList :movies='movies'/>
    <h1>장르</h1>
    <MovieList :movies='movies'/>
    <h1>장르</h1>
    <MovieList :movies='movies'/>
    <h1>장르</h1>
    <MovieList :movies='movies'/>

  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/api/v1/movies'

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