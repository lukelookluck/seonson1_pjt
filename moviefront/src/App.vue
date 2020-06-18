<template>
 <div id="app">
   {{selected_user}}
    <b-navbar id="my-nav" toggleable="lg" type="white" class="text-white">
      <b-navbar-brand to="/">지녀비와 거누의 영화 추천 사이트</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav v-if="isLogin">
          <b-nav-item href="#" @click="logout">로그아웃</b-nav-item>
          <!-- <b-nav-item href="#" to="/community/create">게시글 작성</b-nav-item> -->
          <b-nav-item href="#" to="/">영화 평가하기</b-nav-item>
          <b-nav-item to="/recomand/">취향분석</b-nav-item>
          <b-nav-item to="/movie/MovieDataInsert/">asdad</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav v-else>
          <b-nav-item href="#" to="/accounts/login">로그인</b-nav-item>
          <b-nav-item href="#" to="/accounts/signup">회원가입</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="구현ing.."></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form>
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
    <b-alert v-model="showDismissibleAlert" variant="danger" dismissible>
      ID가 존재하지 않거나 비밀번호가 일치하지 않습니다. 다시 시도해주세요.
    </b-alert>
    <b-alert v-model="showDismissibleAlert2" variant="succse" dismissible>
      회원가입이 완료되었습니다. 로그인해주세요.
    </b-alert>
    <router-view
      :selected_user="selected_user"
      :username="username"
      :article="$route.fullPath"
      :movie="$route.fullPath"
      @data-load="data_load"
      :articles="articles"
      :selected_movie="selected_movie"
      :selected_article="selected_article"
      @show-article="get_article"
      :comments="comments"
      @submit-comment-data="createComment"
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
      showDismissibleAlert: false,  
      showDismissibleAlert2: false,
      selected_user: null,
      isLogin: false,
      like_count: null,
      movies: [],
      recomand_movies: [],
      recomand_movies2: [],
      articles: [],
      selected_movie: null,
      selected_article: null,
      comments: [],
      commentData: [],
      num: 0,
      username: "",
      loginData: {
        username: "",
        password: ""
      },
    };
  },
  created() {
    if (this.$cookies.isKey("auth-token")) {
      this.isLogin = true;
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .get(`${BACK_URL}/accounts/get_username/`, requestHeaders)
        .then(res => {
          console.log(res.data);
          this.username = res.data;
        })
        .catch(err => {
          console.log(err);
        });
      // this.username =
    } else {
      this.isLogin = false;
      this.username = "게스트";
      this.$router.push("/accounts/login");  
    }
    // this.data_load;
    // this.recomand();
    // this.recomand2();
  },
  methods: {
    showAlert() {
        this.dismissCountDown = this.dismissSecs
      },
    data_load($state) {
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      console.log($state);
      axios
        .get(`${BACK_URL}/movies/${this.num}/`, requestHeaders)
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
          console.log(res);
          this.setCookie(res.data.key);
          this.$router.push("/");
          console.log(loginData);
          this.username = loginData.username;
          const requestHeaders = {
            headers: {
              Authorization: `Token ${this.$cookies.get("auth-token")}`
            }
          };
          axios.get(`${BACK_URL}/rest-auth/user/`, requestHeaders).then(res => {
            console.log("damslkdnaslkdnkasj", res.data.username);
            this.username = res.data.username;
            console.log(this.username);
          });
          this.showDismissibleAlert=false
        })
        .catch(err => {
          this.showDismissibleAlert=true
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
          this.username = "게스트";
          this.$router.push("/accounts/first");
        })
        .catch(err => {
          console.error(err.response);
        });
    },
    signup(signupData) {
      console.log(signupData);

      axios
        .post(`${BACK_URL}/rest-auth/signup/`, signupData)
        .then(res => {
          console.log("snakjndjkasndjkasndkjanskjd")
          console.log(signupData);
          this.setCookie(res.data.key);
          this.loginData.username = signupData.username
          this.loginData.password = signupData.password1
          console.log(this.loginData)
          this.login(this.loginData)
        })
        .catch(err => {
          console.log(signupData);
          // this.showDismissibleAlert2=true


          console.error(err.response);
        });
    },
    create(articleData) {
      console.log(articleData);
      const reqeustHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      articleData.uesrname = this.username
      axios
        .post(`${BACK_URL}/community/create/`, articleData, reqeustHeaders)
        .then(res => {
          this.$router.go(-1);
          // this.$router.push({
          //   name: "MovieDetailView",
          //   params: {
          //     id: articleData.id
          //     // selectedMovie: articleData
          //     // selectedMovie: x,
          //   }
          // });
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
          console.log("아티클 데이터", res.data);
          this.articles = res.data;
        })
        .catch(err => {
          console.log(err.response);
        });
    },
    get_article(movie, article) {
      console.log(article);
      this.selected_article = article;
      console.log(this.selected_article);
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      // console.log(requestHeaders)
      console.log(movie.id);
      console.log(article.id);
      axios
        .get(`${BACK_URL}/community/${article.id}`, article, requestHeaders)
        .then(res => {
          console.log(res);
          this.selected_article = res.data;
          console.log(this.selected_article)
          axios
            .get(`${BACK_URL}/movies/get_value/${article.user}/${movie.id}`, article, requestHeaders)
            .then(res => {
              console.log("get_value", res);
              this.selected_user = res.data;
              axios
                .get(
                  `${BACK_URL}/community/${movie.id}/${article.id}/comments`,
                  article,
                  requestHeaders
                )
                .then(res => {
                  console.log(res);
                  this.comments = res.data;
                  this.$router.push({
                    name: "ArticleDetail",
                    params: {
                      movie: movie.id,
                      article: article.id
                    }
                  });
                });
            });
        });
    },
    go_detail_movie(movie) {
      this.selected_movie = movie;
      this.$router.push({
        name: "MovieDetailView",
        params: {
          movie: movie.id
          // selectedMovie: movie
        }
      });
    },
    createComment(commentData) {
      this.commentData = commentData;
      // console.log(this.commentData.article_id)
      console.log(commentData);
      // console.log(this.commentData)
      const reqeustHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .post(
          `${BACK_URL}/community/${this.commentData.article}/comment_create/`,
          commentData,
          reqeustHeaders
        )
        .then(res => {
          // this.$router.push({ name: "ArticleDetail" });
          this.comments.unshift(res.data);
          console.log(res.data);
        })
        .catch(err => {
          console.log(err.response.data);
        });
    }
  }
};
</script>


<style>
#app {
  font-family: "Noto Sans KR", sans-serif, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: #ebeef1;
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
#my-nav {
  background: linear-gradient( to left, #1ea1f7, #46cfa7 );
}

.navbar-white .navbar-nav .nav-link {
  color: white;
}

.navbar-white .navbar-nav .nav-link:hover {
  color: #1e56b3;
}

.navbar-white .navbar-brand {
  color: white;
}

.navbar-white .navbar-brand:hover {
  color: #1e56b3;
}
</style>
