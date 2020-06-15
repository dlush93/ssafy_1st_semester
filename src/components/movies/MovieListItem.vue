<template>
  <div class="item">
    <img :src="IMG_URL" alt="" width="100%" @click="movieClick">
    <p>{{ movie.title }}</p>
  </div>
</template>

<script>
const MAIN_URL = 'https://image.tmdb.org/t/p/w342/'

export default {
  name: 'MovieListItem',
  props: {
    movie: {
      type: Object
    }
  },
  computed: {
     IMG_URL() { return MAIN_URL+this.movie.poster_path } 
  },
  methods: {
    movieClick() {
      this.$router.push({ name: 'MovieDetail', params: {id: this.movie.id }})
    }
  }
}
</script>

<style>

</style>