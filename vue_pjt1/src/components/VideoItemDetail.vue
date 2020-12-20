<template>
  <div class=" mx-auto my-3" >
      <div class="my-3 text-center">{{video.snippet.title}}</div>
    <div class="embed-responsive embed-responsive-16by9 w-75 mx-auto">
        
    <iframe class="embed-responsive-item"  :src="youtubeUrl" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>
  </div>
</template>

<script>
export default {
    name : 'VideoItemDetail',
    props :{
        video : {
            type : Object
        }
    },
    computed : {
    youtubeUrl(){
      const url = 'https://www.youtube.com/embed/'
      //return `https://www.youtube.com/embed/${this.videoDetail.id.videoId}`
      return url + this.video.id.videoId
    }
    }
}
</script>

<style>

</style>