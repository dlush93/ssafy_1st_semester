<template>

  <div id="app" class="d-flex w-100 h-100 p-3 mx-auto flex-column">
    <header class="masthead mb-auto">
      <div class="inner">
        <h3 class="masthead-brand">MMM</h3>
        <nav class="nav nav-masthead justify-content-center">
          <router-link to="/" class="nav-link hover-item" :class="{active : isactive.MovieList}">목록으로</router-link>
          <router-link v-show="!isLogined" to="/login" class="nav-link hover-item" :class="{active : isactive.LoginView}">Login</router-link>
          <router-link v-show="!isLogined" to="/signup" class="nav-link hover-item" :class="{active : isactive.SignupView}">Signup</router-link>
          <router-link v-show="isLogined" to="/logout" class="nav-link hover-item" :class="{active : isactive.LogoutView}">로그아웃</router-link>
        </nav>
      </div>
    </header>

    <main role="main" class="inner cover" :class="{container : !isactive.MovieList}">
      <router-view @submit-login="login" @submit-signup="signup" @submit-logout="logout"/>
    </main>

    <footer class="mastfoot mt-auto">
      <div class="inner">
        <p>Cover template for <a href="https://getbootstrap.com/">Bootstrap</a>, by <a href="https://twitter.com/mdo">@mdo</a>.</p>
      </div>
    </footer>
  </div>
</template>


<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'App',
  data() {
    return {
      isLogined: false,
      isactive : {
        'MovieList' : false,
        'LoginView' : false,
        'SignupView' : false,
        'LogoutView' : false,
      }
      
    }
  },
  methods: {
    cookies_set(key) {
      this.$cookies.set('auth-token',key)
      this.isLogined = true
    },
    login(loginData) {
      axios.post(API_URL + '/rest-auth/login/', loginData)
        .then((res)=>{
          this.cookies_set(res.data.key)
          this.$router.push('/articles')
        })
        .catch((err)=>{
          console.log(err.response)
        })
    },
    logout() {
      const request_header = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(API_URL + '/rest-auth/logout/', null, request_header)
        .then((res)=>{
          console.log(res)
          this.isLogined = false
          this.$cookies.remove('auth-token')
          this.$router.push('/articles')
        })
        .catch((err)=>{
          console.log(err.response)
        })
    },
    signup(signupData) {
      axios.post(API_URL + '/rest-auth/signup/', signupData)
        .then((res)=>{
          this.cookies_set(res.data.key)
          this.$router.push('/articles')
        })
        .catch((err)=>{
          console.log(err.response)
        })
    },
    logincheck() {
      if(this.$cookies.isKey('auth-token')) {
        this.isLogined = true
      }
    },
    routercheck(){
      for (var element in this.isactive){
        if (element == this.$router.currentRoute.name){
          this.isactive[element] = true
        } else{
          this.isactive[element] = false
        }
      }
    }
  },
  mounted() {
    this.logincheck()
    this.routercheck()
  },
  updated(){
    this.routercheck()
  }
}
</script>

<style>
  @import './assets/cover.css';
  .hover-item:hover {
    color: #ffffff
  }
</style>
