<template>
  <div class="col-12 my-2">
    <div class="row">
      <div class="col-2">
        작성 내용 : 
      </div>
      <div class="col-5">
        {{comment.content}}
      </div>
      <div class="col-2">
        작성자 : {{comment.user.username}}
      </div>
      <button v-if="comment.user.username === loginusername" class="btn btn-primary mx-2"  data-toggle="modal" :data-target="`#comment${comment.id}`">수정</button>
      <button v-if="comment.user.username === loginusername" class="btn btn-primary" @click="deletecomment">삭제</button>
    </div>

    <!-- 수정 모달 부분 -->
    <div class="modal fade" :id="`comment${comment.id}`" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">댓글 수정</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body" >
            댓글내용 : <input class="col-8" v-model="commentModify" type="text">
            
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" @click="changeComment">수정 완료</button>
            <button type="button"  :id="`delete${comment.id}`"  class="btn btn-secondary" data-dismiss="modal">닫기</button>
          </div>
        </div>
      </div>
</div>

  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000/'
export default {
  name : 'CommentList',
  data(){
    return {
      loginusername : null,
      commentModify : ''
    }
  },
  props : {
    comment : {
      type : Object
    }
  },
  methods : {
    logincheck() {
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      if(this.$cookies.isKey('auth-token')) {
        axios.post(`${API_URL}accounts/`,null,request_header)
          .then((res)=> {
            this.loginusername = res.data.username
          })
      }
    },
    inputComment(){
      this.commentModify = this.comment.content
    },
    changeComment(){
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      const deletebtn = document.querySelector(`#delete${this.comment.id}`)
      axios.put(`${API_URL}api/v1/community/commentlist/${this.comment.id}/`,{'content': this.commentModify},request_header)
      .then(()=>{
        deletebtn.click()
        this.$router.push({name:'CommunityView'})
      })
    },
    deletecomment(){
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.delete(`${API_URL}api/v1/community/commentlist/${this.comment.id}/`,request_header)
      .then(()=>{
        alert('삭제되었습니다.')
        this.$route.go()
      })
    }
  },
  created(){
    this.logincheck()
    this.inputComment()
  }

}
</script>

<style>

</style>