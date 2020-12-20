<template>
  <div>
      <input type="text" v-model="input" @keypress.enter="onSearch">
      <button @click="onSearch">검색</button>
  </div>
</template>

<script>
export default {
    name: 'VideoSearch',
    data(){
        return{
            input: '',
        }
    },
    methods: {
        onSearch(){
            this.$emit('search_name', this.input)
            this.input = ''
        }
    }


}
</script>

<style>

</style>