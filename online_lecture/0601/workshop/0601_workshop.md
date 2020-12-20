# 0601_workshop





#### App.vue

```html
<template>
  <div class="container">
    <p>유튜브 클론코딩</p>
    <SearchBar @search-list="onSearchList"/>
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'
import axios from 'axios'

const API_KEY = 'AIzaSyCUL0UB017Lfxblyns5O6XQ5d9bfFN5QHI'
const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  data(){
    return {
      videos : []
    }
  },
  components: {
    SearchBar
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
      
          this.videos = res.data.items
      })

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





#### SearchBar.vue

```vue
<template>
  <div>
    <input  type="text" v-model="inputData" @keypress.enter="onsearch"> 
    <button @click="onsearch">검색</button>
  </div>
</template>

<script>
export default {
  name : 'SeachBar',
  data(){
    return {
      inputData : '',
    }
  },
  methods : {
    onsearch(){
  
      this.$emit('search-list',this.inputData)
      this.inputData = ''

    }
  }
  
}
</script>

<style>

</style>
```

