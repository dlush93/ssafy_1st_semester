<template>
  <div id="app">
    <div>
      <button @click="statusIndex">Index</button>|
      <button @click="statusLotto">Lotto</button>
    </div>
    <Index v-if="status === 'index'"/>
    <Lotto v-if="status === 'lotto'"/>
  </div>
</template>

<script>
/// 두번째 단계:  불러오기

import Index from "./components/Index.vue"
import Lotto from "./components/Lotto.vue"

export default {
  name: 'App',
  components: {
    Index,
    Lotto,
  },
  data : function() {
      return {
        status : 'index'
      }
    },
    methods : {
      statusLotto : function() {
        this.status = 'lotto'
      },
      statusIndex : function () {
        this.status = 'index'
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
