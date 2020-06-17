<template>
  <div class="container">
    <img alt="Vue logo" src="../../../src/assets/unnamed.gif" />
    <div class="text-left">
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group id="input-group-1" label="username:" label-for="input-1">
          <b-form-input
            id="input-1"
            v-model="loginData.username"
            type="text"
            required
            placeholder="Enter username"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="password:" label-for="input-2">
          <b-form-input id="input-2" type="password" v-model="loginData.password" required placeholder="Enter name"></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">로그인</b-button>
        <b-button type="reset" variant="danger">초기화</b-button>
      </b-form>
    </div>
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
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.loginData.username = "";
      this.loginData.password = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>

<style>
</style>