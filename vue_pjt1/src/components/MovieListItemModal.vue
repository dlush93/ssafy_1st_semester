<template>
  <div class="modal fade" :id="movieId" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title h3" id="exampleModalLabel">{{movie.title}}</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
          <img :src="movieBackdropUrl" alt="" class="w-100">
          <hr>
          <h4><span class = "col-2 badge badge-success ">
              {{movie.user_rating}}
          </span>
          </h4>

          <div class="mt-3">
             {{movie.overview}}
          </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
    name: "MovieListItemModal",
    props :{
        movie : {
            type :Object
        }
    },
    computed : {
        movieId(){
            return "movie"+this.movie.id
        },
        movieBackdropUrl(){
            return this.movie.backdrop_url
        }
    }

}
</script>

<style>

</style>