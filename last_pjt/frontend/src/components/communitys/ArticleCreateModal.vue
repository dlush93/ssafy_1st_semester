<template>
  <div class="modal fade" :id="'Modal'" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">새글 작성</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body text-left">
          <div>
            <label for="title">제목</label><br>
            <input type="text" id="title" width="100%" v-model="articleData.title" placeholder="제목을 작성하세요">
          </div>
          <hr>
          <label for="content">내용</label><br>
          <textarea name="" id="content" cols="50" rows="10" v-model="articleData.content" placeholder="내용을 작성하세요"></textarea>
        </div>
        <div class="modal-footer">
          <button class="btn btn-primary" @click="createArticle" data-dismiss="modal" aria-label="Close">제출</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const BASE_URL = 'http://127.0.0.1:8000/'
const API_URL = BASE_URL+`api/v1/community/`

export default {
  name: 'ArticleCreateModal',
  data() {
    return {
      user: null,
      articleData: {
        title: '',
        content: ''
      }
    }
  },
  props: {
    communityid: {
      type: Number 
    }
  },
  methods: {
    createArticle() {
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`,
        }
      }
      axios.post(API_URL+this.communityid+'/articles/', this.articleData, request_header)
        .then((res)=>{
          if(res.data.message) {
            alert(res.data.message)
          }
          this.$emit('createArticle')
          this.articleData.title = ''
          this.articleData.content = ''
        })
    },
  },
  created() {
  }
}
</script>

<style>

</style>