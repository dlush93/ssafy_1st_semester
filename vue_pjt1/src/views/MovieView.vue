<template>
  <div class="container">
      <div class="row">
            <h1 class="col-12 text-center">나만의 무비 컬렉션</h1>
            <MovieList :movieList="movieList"/>
    
            <button v-show="!movieList" class="col-4 offset-4" @click="movieSelect">영화가져오기</button>
      </div>
      
  </div>

</template>

<script>
import axios from 'axios'
import MovieList from '@/components/MovieList.vue'

export default {
    name: 'MovieView',
    data() {
        return {
            movieList: '',

        }
    },
    methods: {
        movieSelect() {
            axios.get('http://www.json-generator.com/api/json/get/ceNyuXZmwi?indent=2')
                .then((res)=>{
                    this.movieList = res.data
                })
        }
    },
    components: {
        MovieList,
    },

}
</script>

<style>

</style>