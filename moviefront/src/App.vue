<template>
  <div id="app">
    <h2>검색기능 구현해 말아?</h2>
    <!-- <div id="nav"> -->
      <!-- <router-link to="/">홈</router-link>| -->
      <!-- <router-link to="/movie/MovieDataInsert">무비데이터 수집</router-link> | -->
    <b-navbar toggleable="lg" type="light" variant="warning  ">
      <b-navbar-brand to="/">지녀비와 거누의 영화 추천 사이트</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav v-if="isLogin">
            
            <b-nav-item href="#" @click="logout">로그아웃</b-nav-item>
            <b-nav-item href="#" to="/community/create">게시글 작성</b-nav-item>
            <b-nav-item href="#" to="/">영화 평가하기</b-nav-item>
            <b-nav-item href="#" to="/movie/recomand">취향분석  </b-nav-item>
        </b-navbar-nav>
 
        <b-navbar-nav v-else>
            <b-nav-item href="#" to="/accounts/login">로그인</b-nav-item>
            <b-nav-item href="#" to="/accounts/signup">회원가입</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form>

          <!-- <b-nav-item-dropdown text="Lang" right>
            <b-dropdown-item href="#">EN</b-dropdown-item>
            <b-dropdown-item href="#">ES</b-dropdown-item>
            <b-dropdown-item href="#">RU</b-dropdown-item>
            <b-dropdown-item href="#">FA</b-dropdown-item>
          </b-nav-item-dropdown> -->

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>{{ username }} 님</em>
            </template>
            <b-dropdown-item v-if="isLogin" href="#">Profile</b-dropdown-item>
            <b-dropdown-item v-if="!isLogin" to="/accounts/login">로그인</b-dropdown-item>
            <b-dropdown-item v-if="!isLogin" to="/accounts/signup">회원가입</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!-- <div id="nav">
      <span v-if="isLogin">
        <router-link to="/">홈</router-link>|
        <router-link to="/accounts/logout" @click.native="logout">로그아웃</router-link>|
        <router-link to="/community/create">게시글 작성</router-link>|
        <router-link to="/">영화 평가하기</router-link>|
        <router-link to="/movie/recomand">취향분석</router-link>|
      </span>
      <span v-else>
        <router-link to="/accounts/login">로그인</router-link>|
        <router-link to="/accounts/signup">회원가입</router-link>|
      </span>
    </div> -->
    <router-view
      @data-load="data_load"
      :articles="articles"
      :selected_movie="selected_movie"
      :selected_article="selected_article"
      @show-article="get_article"
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
import axios from "axios";
// import Vue from 'vue'
// import MovieDetailView from './views/community/MovieDetailView.vue'

const BACK_URL = "http://127.0.0.1:8000";

export default {
  name: "App",

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
      num: 0,
      username: '게스트',
    };
  },
  created() {
    if (this.$cookies.isKey("auth-token")) {
      this.isLogin = true;
    } else {
      this.isLogin = false;
      this.$router.push("/accounts/first");
    }
    this.data_load
    // axios
    //   .get(`${BACK_URL}/movies/${this.num}/`)
    //   .then(res => {
    //     this.movies = res.data;
    //     console.log(this.movies);
    //     // console.log(res.data.re  sults);
    //     console.log(res.data);
    //   })
    //   .catch(err => {
    //     console.log(err);
    //   });
  },
  methods: {
    data_load($state) {
       const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      console.log($state);
      axios.get(`${BACK_URL}/movies/${this.num}/`, requestHeaders)
      .then(({ data }) => {
        if (data.hits.length) {
          this.num += 1;
          this.list.push(...data.hits);
          $state.loaded();
        } else {
          $state.complete();
        }
      });
    },
    setCookie(key) {
      this.$cookies.set("auth-token", key);
      this.isLogin = true;
    },
    login(loginData) {
      axios
        .post(`${BACK_URL}/rest-auth/login/`, loginData)
        .then(res => {
          this.setCookie(res.data.key);
          this.$router.push("/");
          console.log(loginData)
          this.username = loginData.username
        })
        .catch(err => {
          console.error(err.response);
        });
    },
    logout() {
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      console.log(this.$cookies.get("auth-token"));
      axios
        .post(`${BACK_URL}/rest-auth/logout/`, null, requestHeaders)
        .then(() => {
          this.$cookies.remove("auth-token");
          this.isLogin = false;
          this.$router.push("/accounts/first");
        })
        .catch(err => {
          console.error(err.response);
        });
    },
    signup(signupData) {
      axios
        .post(`${BACK_URL}/rest-auth/signup/`, signupData)
        .then(res => {
          // console.log(signupData)
          // console.log(res)
          this.setCookie(res.data.key);
          this.$router.push("/");
        })
        .catch(err => {
          console.log(signupData);

          console.error(err.response);
        });
    },
    create(articleData) {
      const reqeustHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .post(`${BACK_URL}/community/create/`, articleData, reqeustHeaders)
        .then(res => {
          this.$router.push({ name: "ArticleListView" });
          console.log(res.data);
        })
        .catch(err => {
          console.log(err.response.data);
        });
    },
    likeMovie(likeMovieData) {
      const reqeustHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      // this.likeMovieData = likeMovieData
      // console.log(likeMovieData)
      axios
        .post(`${BACK_URL}/movies/like/`, likeMovieData, reqeustHeaders)
        .then(res => {
          console.log(res.data);
          // Vue.set(vm.movies, indexOfMovies, like)
        })
        .catch(err => {
          console.log(err.response);
        });
    },
    insertMovieData(insertData) {
      const reqeustHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      console.log("APP", insertData);
      axios
        .post(`${BACK_URL}/movies/create/`, insertData, reqeustHeaders)
        .then(res => {
          console.log(res.data);
        })
        .catch(err => {
          console.log(err.response.data);
        });
    },
    insertGenreData(insertData) {
      const reqeustHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      console.log("APP", insertData);
      axios
        .post(`${BACK_URL}/movies/genre_create/`, insertData, reqeustHeaders)
        .then(res => {
          console.log(res.data);
        })
        .catch(err => {
          console.log(err.response);
        });
    },
    rateMovie(insertData) {
      const reqeustHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      console.log(reqeustHeaders);

      axios
        .post(`${BACK_URL}/movies/rate/`, insertData, reqeustHeaders)
        .then(res => {
          console.log(res.data);
        })
        .catch(err => {
          console.log(err.response.data);
        });
    },
    recomand() {
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      console.log(requestHeaders);
      axios
        .get(`${BACK_URL}/movies/recomand/`, requestHeaders)
        .then(res => {
          console.log(res.data);
          this.recomand_movies = res.data;
        })
        .catch(err => {
          console.log(err.response);
        });
    },
    recomand2() {
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      console.log(requestHeaders);
      axios
        .get(`${BACK_URL}/movies/recomand2/`, requestHeaders)
        .then(res => {
          console.log(res.data);
          this.recomand_movies2 = res.data;
        })
        .catch(err => {
          console.log(err.response);
        });
    },
    get_movie_articles(movie) {
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      console.log(requestHeaders);
      axios
        .get(
          `${BACK_URL}/community/${movie.id}/articles/`,
          movie,
          requestHeaders
        )
        .then(res => {
          console.log(res.data);
          this.articles = res.data;
        })
        .catch(err => {
          console.log(err.response);
        });
    },
    get_article(movie, article) {
      console.log(movie, article)
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(`${BACK_URL}/community/${article.id}`, article.id, requestHeaders)
      .then(res => {
        console.log(res)
        this.$router.push({
        name: "ArticleDetail",
        params: {
          id: movie.id,
          // selectedMovie: x,
        }
        });

        // this.articles = res.data
      })
      .catch(err => {
        console.log(err.response)
      })
    },
    go_detail_movie(movie) {
      this.selected_movie = movie;
      this.$router.push({
        name: "MovieDetailView",
        params: {
          id: movie.id,
          selectedMovie: movie
          // selectedMovie: x,
        }
      })


    }
  }
};
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
