<template>
  <div class="container">
    <h1>Signup</h1>
    <form class="text-left" >
      <div class="form-group">
        <label>username</label>
        <input
          class="form-control"
          type="text"
          placeholder="username"
          v-model="signupData.username"
        />
        <small id="usernameHelp" class="form-text text-muted">아이디 작성하삼!!</small>
      </div>
      <div class="form-group">
        <label>password</label>
        <input
          class="form-control"
          type="password"
          placeholder="password"
          v-model="signupData.password1"
        />
        <small id="passwordHelp" class="form-text text-muted">비번 작성하삼!!</small>
      </div>
      <div class="form-group">
        <label>password_confirmation</label>
        <input
          class="form-control"
          type="password"
          placeholder="password_confirmation"
          v-model="signupData.password2"
          @keyup.enter="signup"
        />
        <small id="password_confirmationHelp" class="form-text text-muted">비번 똑같이 적으삼!!</small>
      </div>
      <button type="button" @click="signup" class="btn btn-primary" >회원가입</button>
    </form>
  </div>
</template>

<script>
export default {
    name: 'Signup',
    data() {
        return {
            signupData: {
                username: null,
                password1: null,
                password2: null,
            }
        }
    },
    methods: {
        signup() {
            this.$emit('submit-signup-data', this.signupData)
        }
    }
}
</script>

<style>

</style>