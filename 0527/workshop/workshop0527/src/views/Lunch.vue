<template>
  <div>
    <h1>점심 메뉴</h1>
    <button @click="pick">메뉴 추천</button>
    <p>{{menu}}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
data : function (){
  return {
    menus : ['짜장','고기','김치찌개','남다른감자탕','매드포갈릭'],
    menu : '',
  }
},
methods :{
  pick : function(){
    this.menu = _.sample(this.menus)
  }
}

}
</script>

<style>

</style>