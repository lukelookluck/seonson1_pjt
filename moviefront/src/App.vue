<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">홈</router-link> |
      <span v-if="isLogin">
        <router-link to="/accounts/logout" @click.native="logout">로그아웃</router-link> |
        <router-link to="/community/create">게시글 작성</router-link> |
        <router-link to="/community/movie">무비</router-link> |
      </span>
      <span v-else>
        <router-link to="/accounts/login">로그인</router-link> |
        <router-link to="/accounts/signup">회원가입</router-link> |
      </span>
    </div>
    <router-view @submit-article-data="create" @submit-login-data="login" @submit-signup-data="signup" />
  </div>
</template>

<script>
import axios from 'axios'

const BACK_URL = 'http://127.0.0.1:8000'

export default {
  name: 'App',
  data() {
    return {
      isLogin: false
    }
  },
  created() {
    if (this.$cookies.isKey('auth-token')) {
      this.isLogin = true
    }
    else {
      this.isLogin = false
    }
  },
  methods: {
    setCookie(key) {
      this.$cookies.set('auth-token', key)
      this.isLogin = true
    },
    login(loginData) {
      axios.post(`${BACK_URL}/rest-auth/login/`, loginData)
      .then(res => {
        this.setCookie(res.data.key)
        this.$router.push('/')
      })
      .catch(err => {
        console.error(err.response)
      })
    },
    logout() {
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${BACK_URL}/rest-auth/logout/`, null, requestHeaders)
      .then(() => {
        this.$cookies.remove('auth-token')
        this.isLogin = false
        this.$router.push('/')
      })
      .catch(err => {
        console.error(err.response)
      })
    },
    signup(signupData) {
      axios.post(`${BACK_URL}/rest-auth/signup/`, signupData)
      .then(res => {
        console.log(signupData)
        console.log(res)
        this.setCookie(res.data.key)
        this.$router.push('/')
      })
      .catch(err => {
        console.log(signupData)
      
        console.error(err.response)
      })
    },
    create(articleData) {
      const reqeustHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`${BACK_URL}/community/create/`, articleData, reqeustHeaders)
      .then(res => {
        this.$router.push({name: 'ArticleListView'})
        console.log(res.data)
      })
      .catch(err => {
        console.log(err.response.data)

      })
    }
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
