# 0602_workshop



### APP.vue

```html
<!-- APP.vue-->



<template>
  <div class="container">
    <p>유튜브 클론코딩</p>
    <SearchBar @search-list="onSearchList"/>
    <div class='row'>
    <VideoDetail :videoDetail='videoDetail' class='col-7' />
    <VideoList :class="{'col-4': videoDetail, 'col-12':!videoDetail}"    @video-select="onVideoSelect" class='col-5' :videos="videos" />
    </div>
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'
import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'
import axios from 'axios'

const API_KEY = process.env.VUE_APP_API_KEY
const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  data(){
    return {
      videos : [],
      videoDetail : null,
    }
  },
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  methods : {
    onSearchList(inputData){
      const params ={
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: inputData,

      }
      axios.get(YOUTUBE_URL,{params})
      .then((res) => {console.log(res)
          res.data.items.forEach(item =>{
            const parser = new DOMParser() // Parser을 해준다. 사용자가 쓸수있는데이터로 바꿔준다.
            const doc = parser.parseFromString(item.snippet.title,'text/html')
            console.log(doc)
            item.snippet.title = doc.body.innerText
          })
          this.videos = res.data.items
      })

    },
    onVideoSelect(video){
      this.videoDetail = video
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

```





### VideoDetail.vue

```html
<!--VideoDetail.vue-->

<template>
  <div >
    <div v-if="videoDetail" >
      <div class="embed-responsive embed-responsive-16by9">
        <iframe class="embed-responsive-item"  :src="youtubeUrl" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
      </div>
      
      <div>
        <li v-text="videoDetail.snippet.title"></li>
        <li v-text="videoDetail.snippet.description"></li>
      </div>
    
    </div>
    <div v-else>
     
    </div>
  </div>
</template>

<script>
export default {
  name:'VideoDetail',
  data(){
    return {
      videoId : 'M7lc1UVf-VE'
    }
  },
  props :{
    videoDetail : {
      type:Object,
    }
  },
  computed : {
    youtubeUrl(){
      const url = 'https://www.youtube.com/embed/'
      //return `https://www.youtube.com/embed/${this.videoDetail.id.videoId}`
      return url + this.videoDetail.id.videoId
    }
  },
}



</script>

<style>

</style>
```



### VideoList

```html
<template>
  <div>
    <ul class="list-group">
    <VideoListitem class="py-1" @video-select="onVideoSelect" :video="video" v-for="video in videos" :key="video.etag"/>
    </ul>
  </div>
</template>

<script>
import VideoListitem from './VideoListitem.vue'
export default {
  name : 'VideoList',
  components : {
    VideoListitem
  },
  methods : {
    onVideoSelect(video){
      this.$emit('video-select',video)
    }
  },
  props : {
    videos : {
      type : Array
    }
  }
}
</script>

<style>

</style>
```





### VideoListItem

```html
<template>

  <li class="list-group-item" @click="onVideoSelect">
    <div class="media" style="height:20vh">
      <img :src="thumbnailUrl" alt="" class="align-self-center mr-3">
      <div class="media-body">
       <div class="pt-auto border-bottom" style="height:5vh; font-size:1.5vh; "> <p style="text-overflow: ellipsis;">{{video.snippet.title}}</p></div>

       <div class="text-wrap w-100 text-break pt-4" style="font-size:1.5vh;
          height: 12vh;"><span>{{video.snippet.description}}</span></div>
      </div>
    </div>
  </li>
  
</template>

<script>
export default {
  name : 'VideoListitem',
  props : {
    video : {
      type : Object
    }
  },
  methods : {
    onVideoSelect(){
      this.$emit('video-select',this.video)
    },
  },
  computed :{
    thumbnailUrl(){
      return this.video.snippet.thumbnails.default.url
    }
  }

}
</script>

<style>

</style>
```

