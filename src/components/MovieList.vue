<template>
  <div class="row">
    <MovieListItem v-for="movie in movies" :key='movie.id' :movie='movie' class="col-1 p-1"/>

  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name: 'MovieList',
  components: {
    MovieListItem
  },
  props: {
    movies: {
      type: Array
    }
  },
}
</script>

<style>

</style>