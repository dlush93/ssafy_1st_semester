<template>
  <div class="container">
    <div class="card border-dark col-12 movie">
      <div class="row">
        <img :src="IMG_URL" class="card-img-top col-4 p-0" alt="...">
        <div class="card-body col-8 text-left">
          <h1 class="mb-3">{{ movie.title }}</h1>
          <p class="card-text">{{ movie.overview }}</p>
          <span v-for="genre in movie.genres" :key="genre.id" class="genre-list mr-3">{{ genre.name }}</span>
          <div id="meta-table" class="row mt-3">
            <div class="col-6">
              <p>출시일</p>
              <span class="meta-data">{{ movie.release_date }}</span>
            </div>
            <div class="col-6">
              <p>영화점수</p>
              <span class="meta-data">{{ movie.popularity }}</span>
            </div>
            <div class="col-12 my-3"></div>
            <div class="col-6">
              <p>평점</p>
              <span class="meta-data">{{ movie.vote_average }}</span>
            </div>
            <div class="col-6">
              <p>투표수</p>
              <span class="meta-data">{{ movie.vote_count }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <MovieRankList :movie="movie" />

  </div>
</template>

<script>
import MovieRankList from '@/components/movies/MovieRankList.vue'
import axios from 'axios'

const MAIN_URL = 'https://image.tmdb.org/t/p/original'
const BASE_URL = 'http://127.0.0.1:8000/'
const API_URL = BASE_URL+'api/v1/movies/'

export default {
  name: 'MovieDetail',
  components: {
    MovieRankList,
  },
  data() {
    return {
      movie: {
        'poster_path' : '',
        'title': '',
        'backdrop_path': '',
      },
    }
  },
  methods: {
    getMovie() {
      axios.get(API_URL+this.$route.params.id)
        .then((res)=>{
          this.movie = res.data[0]
          this.setBackground()
        })
        .catch((err)=>{
          console.log(err)
        })
    },
    setBackground() {
      const BACK_URL = MAIN_URL + this.movie.backdrop_path
      document.querySelector('#main-body').style.background = `url(${BACK_URL})`;
    },
    deleteBackground() {
      document.querySelector('#main-body').style.background = '#333';
    }
  },
  computed: {
     IMG_URL() { return MAIN_URL+this.movie.poster_path }
  },
  created() {
    this.getMovie()
  },
  destroyed(){
    this.deleteBackground()
  }
  
}
</script>

<style>
  .movie {
    background: rgba(0,0,0,.85);
  }
  .genre-list {
    display: inline-block;
    color: #00FC87;
    font-size: 1.4em;
    font-family: Oswald,sans-serif
  }
  .meta-data {
    display: block;
    color: #00FC87;
    font-size: 1.6em;
    line-height: 1.1em;
  }
  #meta-table > div > p {
     margin-bottom: 0px;
  }
</style>