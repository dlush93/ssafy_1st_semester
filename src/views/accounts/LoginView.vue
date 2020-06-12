<template>
  <div>
    <h1>Login</h1>
    <div class="form-group">
    <label for="InputUsername1">아이디</label>
    <input type="text" class="form-control" id="InputUsername1" aria-describedby="usernameHelp" v-model="loginData.username">
    <small id="usernameHelp" class="form-text text-muted">아이디를 작성해주세요</small>
    </div>
    <div class="form-group">
      <label for="InputPassword1">비밀번호</label>
      <input type="password" class="form-control" id="InputPassword1" aria-describedby="InputPassword1" v-model="loginData.password">
      <small id="InputPassword1" class="form-text text-muted">비밀번호를 작성해주세요</small>
    </div>
    <button type="submit" class="btn btn-primary" @click="login">확인</button>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      loginData: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login() {
      this.$emit('submit-login',this.loginData)
    },
  },


}
</script>

<style>

</style>