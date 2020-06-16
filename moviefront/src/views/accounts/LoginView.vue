<template>
  <div class="container">
    <img alt="Vue logo" src="../../../src/assets/unnamed.gif" />
    <div class="text-left">
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group id="input-group-1" label="유저 이름:" label-for="input-1">
          <b-form-input
            id="input-1"
            v-model="loginData.username"
            type="text"
            required
            placeholder="유저 이름을 입력하세요"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="비밀번호:" label-for="input-2">
          <b-form-input id="input-2" v-model="loginData.password" type="password" required placeholder="비밀번호를 입력하세요"></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">로그인</b-button>
        <b-button type="reset" variant="danger">회원가입</b-button>
      </b-form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      loginData: {
        username: "",
        password: ""
      },

      show: true
    };
  },
  created() {
    if (this.$cookies.isKey("auth-token")) {
      return this.$router.push("/");
    }
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      this.$emit("submit-login-data", this.loginData);
    },
    onReset() {
      this.$router.push("/accounts/signup");
    }
  }
};
</script>

<style>
</style>