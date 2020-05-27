<template>
  <div>
    <h1>로또 추첨</h1>
    <button @click="pick">추천</button>
    <p>{{lotto_number}}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {

  data : function () {
    return {
      numbers : _.range(1,46),
      lotto_number : '',
    }
      
    },
  methods :{
    pick : function(){
      this.lotto_number=_.sampleSize(this.numbers,6).sort(function(a,b){return a-b})
    }
  }
  

}
</script>

<style>

</style>