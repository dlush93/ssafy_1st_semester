<template>
    <div class="col-12">
        <div class="row">
        <MovieListItem class="col-3" v-for="movie in movieList" :key="movie.id" :movie="movie"/>
        </div>
    </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'
export default {
    name: 'MovieList',
    props: {
        movieList: {
            type: Array,
        }
    },
    components:{
        MovieListItem,
    }
}
</script>

<style>

</style>