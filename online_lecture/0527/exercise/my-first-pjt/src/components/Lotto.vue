<template>
  <div>
      <h1>로또 번호 추첨</h1>
      <button @click="pick">추첨</button>
      <p>{{lucky }}</p>
  </div>
</template>

<script>
// var _ = require('lodash');
import _ from 'lodash'

export default {
    data : function() {
        return { 
            numbers : _.range(1,46),
            lucky : ''
         }
    },
    methods : {
        pick : function (){
            this.lucky = _.sampleSize(this.numbers,6).sort(function(a,b){return a-b})
        }
    }

}
</script>

<style>

</style>