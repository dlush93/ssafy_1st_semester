<template>
  <tr>
    <th scope="row">{{article.id}}</th>
      <td>{{communityname}}</td>
      <td>{{article.title}}</td>
      <td>{{ article.created_at | moment('YYYY-MM-DD HH:mm:ss') }}</td>
  </tr>
</template>

<script>
export default {
  name : 'UserArticleitem',
  data(){
    return {
      communityname :"등업 게시판",
      created_at : ''
    }
  },
  props : {
    article :{
      type : Object
    }
  },
  methods : {
    communitycheck(){
      if (this.article.community === 1){
        this.communityname = "자유게시판"

      }
    },
  },
  created(){
    this.communitycheck()
  },
  updated(){
    this.communitycheck()
  }

}
</script>

<style scoped>
th {
  color : white;
  font-size : 1.2rem
}
td {
  color : white;
  font-size : 1.2rem
}

</style>