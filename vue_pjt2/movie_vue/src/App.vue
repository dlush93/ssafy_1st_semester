<template>
  <div id="app">
    <div id="nav">
      <router-link to="/articles">목록으로</router-link> |
      <router-link v-show="!isLogined" to="/login">Login | </router-link>
      <router-link v-show="!isLogined" to="/signup">Signup</router-link>
      <router-link v-show="isLogined" to="/logout">로그아웃</router-link>
    </div>
    <div class="container">
      <div class="row justify-content-center ">
        <router-view @submit-login="login" @submit-signup="signup" @submit-logout="logout"/>
      </div>
    </div>
    
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
    }
  },
  created() {
    this.logincheck()
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
