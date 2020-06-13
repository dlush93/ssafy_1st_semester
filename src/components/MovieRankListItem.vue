<template>
  <div class="row mx-1 border-bottom">
    <p class="col-3">{{ movierank.rank }}</p>
    <div class="col-9">
      <p class="text-left">{{ movierank.content }}</p>
      <p class="user-data">{{ movierank.user.username }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieRankListItem',
  props: {
    movierank: {
      type: Object
    },
  },
}
</script>

<style>
  .user-data {
    text-align: left;
    font-size: 13px;
    color: #999;
    font-family: 나눔고딕, NanumGothic, 돋움, Dotum, Helvetica, sans-serif;
  }
</style>