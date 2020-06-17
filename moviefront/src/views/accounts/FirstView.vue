<template>
  <div class="container">
    <img alt="2" src="../../../src/assets/2.gif" />
    <img alt="1" src="../../../src/assets/1.gif" />
    <img alt="3" src="../../../src/assets/3.gif" />
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

        <b-form-group id="input-group-2" label="password:" label-for="input-2">
          <b-form-input id="input-2" type="password" v-model="loginData.password" required placeholder="비밀번호를 입력하세요"></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">로그인</b-button>
        <b-button type="reset" variant="danger">회원가입</b-button>
      </b-form>
    </div>
    <img alt="4" src="../../../src/assets/4.gif" />
    <img alt="5" src="../../../src/assets/5.gif" />
    <img alt="6" src="../../../src/assets/6.gif" />
  </div>
</template>

<script>
export default {
  name: "FirstView",
  data() {
    return {
      loginData: {
        username: "",
        password: ""
      },

      show: true
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      this.$emit("submit-login-data", this.loginData);
    },
    onReset() {
      this.$router.push('/accounts/signup')
      }
    }
  }

</script>

<style>
</style>