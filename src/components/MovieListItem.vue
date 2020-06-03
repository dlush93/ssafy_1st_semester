<template>
  <div>
     <div class="card" style="width: 18rem;">
  <img :src="movieUrl" class="card-img-top p-2" alt="...">
  <div class="card-body">
    <p class="card-text">{{movie.title}}</p>
    <button type="button" class="btn btn-warning"  data-toggle="modal" :data-target="movieId">영화정보 상세보기</button>
    <MovieListItemModal :movie="movie"/>
  </div>
</div>
  </div>
</template>

<script>
import MovieListItemModal from "@/components/MovieListItemModal.vue"
export default {
    name: 'MovieListItem',
    props: {
        movie: {
            type: Object
        }
    },
    computed :{
        movieUrl(){
            return this.movie.poster_url
        },
        movieId(){
            return '#movie'+this.movie.id
        }
    },
    components :{
        MovieListItemModal,
    }

}
</script>

<style>

</style>