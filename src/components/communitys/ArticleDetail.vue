<template>
  <div>
    <div class="row articleHead p-2 text-center mb-3">
      <p class="mb-0">{{ article.user.username }}</p>
      <p class="mx-auto mb-0">{{ article.created_at | moment('YYYY-MM-DD HH:mm') }}</p>
      <p class="mb-0">추천수</p>
    </div>
    <div class="blog-main">
      <div class="blog-post mb-5">
        <h2 class="blog-post-title">{{ article.title }}</h2>
        <hr>
      </div>

      <div class="blog-post">
        <p v-html="article.content"></p>
        <hr class="mt-3">
      </div>
      
      <nav class="blog-pagination mbt-5">
        <button class="btn btn-outline-primary" :class="{likestatus: this.likestatus}" @click="like"> 추 천 </button>
        <p class="btn btn-outline-secondary disabled m-0"> {{ article.like_users_count }}명</p>
        <button v-if="article.user.username === username" class="btn btn-primary mx-2"  data-toggle="modal" :data-target="`#article${article.id}`">수정</button>
        <button v-if="article.user.username === username" class="btn btn-primary" @click="deleteArticle"  >삭제</button>
      </nav>

       <!-- 수정 모달 부분 -->
    <div class="modal fade" :id="`article${article.id}`" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">게시글 수정</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body" >
            제목 : <input class="col-8" v-model="article.title" type="text">
            <div class="w-100"></div>
            내용 : <textarea name="content" id="" cols="30" rows="10" v-model="modifycontent" > </textarea>
            
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" @click="changearticle">수정 완료</button>
            <button id="delete" type="button" class="btn btn-secondary" data-dismiss="modal">닫기</button>
          </div>
        </div>
      </div>
    </div>





      <h2 class="text-left">댓글 작성</h2>
      <div class="col-12 mt-2">
        <input class="col-9" type="text" v-model="commentSend" @keyup.enter="writeComment">
        <input class="offset-1" type="submit" value="작성" @click="writeComment">
      </div>
      <div v-if="isSuperuser" >
          <button class="btn btn-outline-primary" @click="gradeup">등업 시키기</button>
      </div>

      <div class="d-flex">
        <p class="text-left mb-0">댓글</p>
        <span class="mx-3"> | </span>
        <p class="mb-0">총 : {{ comment_count }}개</p>
      </div>
      <hr class="my-1">


      <div class="container">
        <div class="row">
          <CommentList :comment="comment" v-for="comment in comments" :key="comment.id" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommentList from '@/components/communitys/CommentList.vue'
const BASE_URL = 'http://127.0.0.1:8000/'
const LIKE_URL = BASE_URL+'api/v1/community/like/'
const USER_URL = BASE_URL+'accounts/'
const GRADE_URL = BASE_URL+'accounts/grade/'
export default {
  name: 'ArticleDetail',
  data() {
    return {
      article: this.$route.params.article,
      likestatus : false,
      username: '',
      isSuperuser: false,
      commentSend: '',
      comments : [],
      modifycontent : '',
    }
  },
  props :{
    community : {
      type : Object
    }
  },
  methods: {
    getUser() {
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`,
        }
      }
      axios.post(USER_URL,null,request_header)
        .then((res)=>{
          this.username = res.data.username
        })
    },
    like() {
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`,
        }
      }
      axios.post(LIKE_URL+this.article.id,null,request_header)
        .then((res)=>{
          this.likestatus = res.data.likestatus
          console.log(res.data.likestat)       
          this.article.like_users_count += res.data.likestat
          alert(res.data.message)
        })
    },
    gradeup(){
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(GRADE_URL+this.article.user.username+'/',null,request_header)
      .then((res)=>{
        console.log(res.data)
        alert(res.data.message)
    
      })
    },
    getSuperuser(){
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post('http://127.0.0.1:8000/accounts/superuser/',null,request_header)
      .then(res=>{
        this.isSuperuser = res.data.status
      })

    },
    writeComment(){
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(BASE_URL+'api/v1/community/'+this.article.id+'/comments/',{'content' : this.commentSend},request_header)
      .then(res=>{
        this.commentSend = ""
        console.log(res.data)
      })
    },
    getCommentList(){
      axios.get(BASE_URL+'api/v1/community/comments/'+this.article.id)
      .then(res=>{
        this.comments = res.data
      })
    },
    modifyarticlecontent(){
      this.modifycontent=this.article.content.replace(/<br>/g, '\r\n')
    },
    changearticle(){
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      const deletebtn = document.querySelector('#delete')

      axios.put(`${BASE_URL}api/v1/community/articleslist/${this.article.id}/`,{'title': this.article.title,
        'content': this.modifycontent},request_header)
      .then(()=>{
        deletebtn.click()
        const communitybtn = document.querySelector(`#community1`)
        communitybtn.click()
      })
    },
    deleteArticle(){
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.delete(`${BASE_URL}api/v1/community/articleslist/${this.article.id}/`,request_header)
      .then(()=>{
        const communitybtn = document.querySelector(`#community1`)
        communitybtn.click()
      })

    }
  },
  components : {
    CommentList,
  },
  mounted(){
    this.getUser()
    this.getSuperuser()
    this.getCommentList()
    this.modifyarticlecontent()
  },
  computed : {
    comment_count : function() {
      return this.comments.length
    }
  }
}
</script>

<style>
  .likestatus {
    background: red ;
    color: seashell;
    border: red;
  }

</style>