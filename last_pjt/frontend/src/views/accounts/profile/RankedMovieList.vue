<template>
  <div>
        <table class="table mt-5">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">평점 영화</th>
          <th scope="col">평점</th>
          <th scope="col">평점 내용</th>
        </tr>
      </thead>
      <tbody>
        <RankedMovieListitem :rankmovie="rankmovie"  v-for="rankmovie in RankeMovieList" :key="rankmovie.id" />
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
import RankedMovieListitem from '@/components/profile/RankedMovieListitem.vue'
const BASE_URL = 'http://127.0.0.1:8000/'
const API_URL = BASE_URL+'accounts/movie_ranks/'
export default {
  name : 'RankedMovieList',
  data(){
    return {
      RankeMovieList :[]
    }
  },
  methods : {
    getRankedMovieList(){
      const username = this.$route.params.username
      axios.get(API_URL+username)
      .then((res)=>{
        this.RankeMovieList = res.data
      })
    }

  },
  created(){
    this.getRankedMovieList()
  },
  components : {
    RankedMovieListitem
  }
}
</script>

<style scoped>
th {
  color: white;
}

</style>