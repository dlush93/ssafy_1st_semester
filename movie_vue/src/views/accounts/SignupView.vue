<template>
  <div>
    <div class="form-group">
    <label for="InputUsername1">아이디</label>
    <input type="text" class="form-control" id="InputUsername1" aria-describedby="usernameHelp" v-model="signupData.username">
    <small id="usernameHelp" class="form-text text-muted">아이디를 작성해주세요</small>
    </div>
    <div class="form-group">
      <label for="InputPassword1">비밀번호</label>
      <input type="password" class="form-control" id="InputPassword1" aria-describedby="InputPassword1" v-model="signupData.password1">
      <small id="InputPassword1" class="form-text text-muted">비밀번호를 작성해주세요</small>
    </div>
    <div class="form-group">
      <label for="InputPassword2">비밀번호 확인</label>
      <input type="password" class="form-control" id="InputPassword2" aria-describedby="InputPassword2" v-model="signupData.password2">
      <small id="InputPassword2" class="form-text text-muted">비밀번호를 다시 한번 입력해주세요</small>
    </div>
    <button type="submit" class="btn btn-primary" @click="signup">확인</button>
  </div>
</template>

<script>
export default {
  name: 'signupView',
  data() {
    return {
      signupData: {
        username: null,
        password1: null,
        password2: null
      }
    }
  },
  methods: {
    signup() {
      this.$emit('submit-signup',this.signupData)
    }
  }
}
</script>

<style>

</style>