<template>
  <div id="app">
    <div id="nav">
      <!-- <router-link to="/">홈</router-link>| -->
      <!-- <router-link to="/movie/MovieDataInsert">무비데이터 수집</router-link> | -->
      <span v-if="isLogin">
        <router-link to="/accounts/logout" @click.native="logout">로그아웃</router-link>|
        <router-link to="/community/create">게시글 작성</router-link>|
        <router-link to="/">영화 평가하기</router-link>|
        <router-link to="/movie/recomand">취향분석</router-link>|
        <!-- <router-link to="/community/movie/:id">무비</router-link> | -->
      </span>
      <span v-else>
        <router-link to="/accounts/login">로그인</router-link>|
        <router-link to="/accounts/signup">회원가입</router-link>|
      </span>
    </div>
    <router-view
      :articles="articles"
      :selected_movie="selected_movie"
      :selected_article="selected_article"
      @submit-article-for-comments="get_article_comments"
      @submit-detail-movie="go_detail_movie"
      @submit-movie-for-articles="get_movie_articles"
      :recomand_movies="recomand_movies"
      :recomand_movies2="recomand_movies2"
      @submit-recomand-request-2="recomand2"
      @submit-recomand-request="recomand"
      @submit-rate-value="rateMovie"
      :movies="movies"
      @submit-genre-data="insertGenreData"
      @submit-movie-data="insertMovieData"
      @submit-like-movie="likeMovie"
      @submit-article-data="create"
      @submit-login-data="login"
      @submit-signup-data="signup"
    />
  </div>
</template>

<script>
import axios from 'axios'
// import Vue from 'vue'
// import MovieDetailView from './views/community/MovieDetailView.vue'

const BACK_URL = 'http://127.0.0.1:8000'

export default {
  name: 'App',
  data() {
    return {
      isLogin: false,
      like_count: null,
      movies: [],
      recomand_movies: [],
      recomand_movies2: [],
      articles: [],
      selected_movie: null,
      selected_article: null,

    }
  },
  created() {
    if (this.$cookies.isKey('auth-token')) {
      this.isLogin = true
    }
    else {
      this.isLogin = false
      this.$router.push('/accounts/first')
    }
    axios.get(`${BACK_URL}/movies/`)
      .then(res => {
        this.movies = res.data;
        console.log(this.movies);
        // console.log(res.data.re  sults);
        console.log(res.data);
      })
      .catch(err => {
        console.log(err.data);
      });
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
      console.log(this.$cookies.get('auth-token'))
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
        // console.log(signupData)
        // console.log(res)
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
        this.$router.push({name: 'MovieDetailView'})
        console.log(res.data)
      })
      .catch(err => {
        console.log(err.response.data)

      })
    },
    likeMovie(likeMovieData) {
      const reqeustHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      // this.likeMovieData = likeMovieData
      // console.log(likeMovieData)
      axios.post(`${BACK_URL}/movies/like/`, likeMovieData, reqeustHeaders)
      .then(res => {
        console.log(res.data)
        // Vue.set(vm.movies, indexOfMovies, like)
      })
      .catch(err => {
        console.log(err.response)

      })
    },
    insertMovieData(insertData) {
      const reqeustHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      console.log("APP", insertData)
      axios.post(`${BACK_URL}/movies/create/`, insertData, reqeustHeaders)
      .then(res => {
        console.log(res.data)
      })
      .catch(err => {
        console.log(err.response.data)

      })

    },
    insertGenreData(insertData) {
      const reqeustHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      console.log("APP", insertData)
      axios.post(`${BACK_URL}/movies/genre_create/`, insertData, reqeustHeaders)
      .then(res => {
        console.log(res.data)
      })
      .catch(err => {
        console.log(err.response)

      })
    },
    rateMovie(insertData) {
      const reqeustHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      console.log(reqeustHeaders)

      axios.post(`${BACK_URL}/movies/rate/`, insertData, reqeustHeaders)
      .then(res => {
        console.log(res.data)
      })
      .catch(err => {
        console.log(err.response.data)
      })
    },
    recomand() {
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      console.log(requestHeaders)
      axios.get(`${BACK_URL}/movies/recomand/`, requestHeaders)
      .then(res => {
        console.log(res.data)
        this.recomand_movies = res.data
      })
      .catch(err => {
        console.log(err.response)
      })
    },
    recomand2() {
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      console.log(requestHeaders)
      axios.get(`${BACK_URL}/movies/recomand2/`, requestHeaders)
      .then(res => {
        console.log(res.data)
        this.recomand_movies2 = res.data
      })
      .catch(err => {
        console.log(err.response)
      })
    },
    get_movie_articles(movie) {
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      console.log(requestHeaders)
      axios.get(`${BACK_URL}/community/${movie.id}/articles/`, movie, requestHeaders)
      .then(res => {
        console.log(res.data)
        this.articles = res.data
      })
      .catch(err => {
        console.log(err.response)
      })
    },
    get_article_comments(movie, article) {
      console.log(article)
      this.selected_article = article
      console.log(this.selected_article)
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      // console.log(requestHeaders)
      console.log(movie.id)
      console.log(article.id)
      axios.get(`${BACK_URL}/community/${movie.id}/${article.id}/comments`,  article, requestHeaders)
      .then(res => {
        console.log(res)
        // this.articles = res.data
      })
      .catch(err => {
        console.log(err.response)
      })
    },
    go_detail_movie(movie) {
      this.selected_movie = movie
      this.$router.push({name: 'MovieDetailView',
        params: {
          id: movie.id,
          selectedMovie: movie
          // selectedMovie: x,
        }
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
