<template>
  <div class="row contanin">
    <MovieListItem v-for="movie in movies" :key='movie.id' :movie='movie' class="col-1 p-1 item"/>

  </div>
</template>

<script>
import MovieListItem from '@/components/movies/MovieListItem.vue'

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

.contanin {
  display: flex;
  margin-top: 50px;
}

.item {
  position: relative;
  display: block;
  flex: 1 1 0px;
  transition: transform 500ms;
}

.contanin:focus-within .item,
.contanin:hover .item {
  transform: translateX(-25%);
}

.item:focus ~ .item,
.item:hover ~ .item {
  transform: translateX(25%);
}

.contanin .item:focus,
.contanin .item:hover {
  transform: scale(1.5);
  z-index: 1;
}

body {
  overflow-x: hidden;
}

.item img {
  display: block;
  max-width: 100%;
}
</style>