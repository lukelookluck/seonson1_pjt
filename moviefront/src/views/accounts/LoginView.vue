<template>
  <div class="container">
    asdasd
    <h1>Login</h1>
    <form class="text-left" >
      <div class="form-group">
        <label>username</label>
        <input
          class="form-control"
          type="text"
          placeholder="username"
          v-model="loginData.username"
        />
        <small id="usernameHelp" class="form-text text-muted">아이디 입력하삼!!</small>
      </div>
      <div class="form-group">
        <label>password</label>
        <input
          class="form-control"
          type="password"
          placeholder="password"
          v-model="loginData.password"
          @keyup.enter="login"
        />
        <small id="passwordHelp" class="form-text text-muted">비번 입력하삼!!</small>
      </div>
      <button type="button" @click="login" class="btn btn-primary" >로그인</button>
    </form>
  </div>
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            loginData: {
                username: null,
                password: null,
            }
        }
    },
    created() {
      if (this.$cookies.isKey('auth-token')) {
          return this.$router.push('/')
      }
    },
    methods: {
        login() {
            this.$emit('submit-login-data', this.loginData)
        }
    }
}
</script>

<style>

</style>