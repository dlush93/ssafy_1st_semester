<template>
  <div>
      <VideoItemDetail :video="video" v-for="video in videos" :key="video.etag" />
      
  </div>
</template>

<script>
import VideoItemDetail from '@/components/VideoItemDetail.vue'
export default {
    name:"VideoItem",
    props :{
        videos : {
            type : Array
        }
    },
    components :{
        VideoItemDetail,
    }

}
</script>

<style>

</style>