<template>
  <div class="container">
    <img alt="2" src="../../../src/assets/2.gif" />
    <img alt="1" src="../../../src/assets/1.gif" />
    <img alt="3" src="../../../src/assets/3.gif" />
    <h1>Signup</h1>
    <div class="text-left">
      <b-form @submit="signup" v-if="show">
        <b-form-group id="input-group-1" label="유저 이름:" label-for="input-1">
          <b-form-input
            id="input-1"
            v-model="signupData.username"
            type="text"
            required
            placeholder="유저 이름을 입력하세요"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="비밀번호:" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="signupData.password1"
            type="password"
            required
            placeholder="비밀번호를 입력하세요"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-3" label="비밀번호 확인:" label-for="input-3">
          <b-form-input
            id="input-3"
            v-model="signupData.password2"
            type="password"
            required
            placeholder="비밀번호를 입력하세요"
          ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">회원가입</b-button>
      </b-form>
    </div>
  <img alt="4" src="../../../src/assets/4.gif" />
  <img alt="5" src="../../../src/assets/5.gif" />
  <img alt="6" src="../../../src/assets/6.gif" />
  </div>
</template>

<script>
export default {
  name: "Signup",
  data() {
    return {
      signupData: {
        username: null,
        password1: null,
        password2: null
      },
      show: true
    };
  },
  methods: {
    signup() {
      this.$emit("submit-signup-data", this.signupData);
    }
  }
};
</script>

<style>
</style>