<template>
  <div class="row mx-1 border-bottom">
    <div class="col-2"> 
      <star-rating class="d-flex" :rating="movierank.rank/2" :star-size="20" :read-only="true" :show-rating="false" :increment="0.1"></star-rating>{{ movierank.rank }} 점
    </div>
    <div class="col-10">
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