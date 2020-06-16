<template>
  <div>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">번호</th>
          <th scope="col">제목</th>
          <th scope="col">작성자</th>
          <th scope="col">작성일</th>
          <th scope="col">추천수</th>
        </tr>
      </thead>
      <tbody>
          <tr v-for="article in articles" :key="article.id" @click="articleItemClick(article.id)">
            <th>{{ article.id }}</th>
            <th>{{ article.title }}</th>
            <th>{{ article.user.username }}</th>
            <th>{{ article.created_at | moment('YYYY-MM-DD HH:mm:ss') }}</th>
            <th></th>
          </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'ArticleList',
  props: {
    articles: {
      type: Array
    }
  },
  methods: {
    articleItemClick(article_id) {
      this.$router.push({ path: 'community/detail', params: {id: article_id }})
    }
  }
}
</script>

<style>

</style>