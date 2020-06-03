<template>
  <div class="container">
      <div class="row  justify-content-center">
      <div class="h1 text-center col-12">영화예고편 검색</div>
        <div class="col-12"></div>
      <VideoSearch  class="mb-5" @search_name="videoList"/>
      <VideoItem class="col-12" :videos="videos"/>
      </div>
  </div>
</template>

<script>
import VideoSearch from '@/components/VideoSearch.vue'
import VideoItem from "@/components/VideoItem.vue"
import axios from 'axios'
const API_KEY = process.env.VUE_APP_API_KEY
// const API_KEY='AIzaSyCoBFRfz2whhTfqf-WbkyRxOPcNMWqt3HU'
const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'
function trim(stringToTrim) {
    return stringToTrim.replace(/^\s+|\s+$/g,"");
}




export default {
    name: 'VideoView',
    data(){
        return {
            videos:[]
        }
    },
    components: {
        VideoSearch,
        VideoItem,
    },
    methods: {
        videoList(input){
            input = trim(input)
            if (input != false) {
            const params ={
                key: API_KEY,
                part : 'snippet',
                type : 'video',
                q : input+' trailer',
            }
            axios.get(YOUTUBE_URL,{params})
            .then((res)=>{
                this.videos = res.data.items
            })
            }
        }
        

    }
}
</script>

<style>

</style>