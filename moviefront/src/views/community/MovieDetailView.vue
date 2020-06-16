<template>
  <div class="container">
    <section class="border">
      <h1>영화 정보 표시할 섹션</h1>
      <img class="d-flex" :src="poster" alt="poster" />
      <div class="rr">
        <h1>{{ selected_movie.title }}</h1>
        {{ selected_movie.release_date }}, {{ selected_movie.genre_ids }}
        장르 id를 db에 접근해서 비교해서 값을 가져와야하는데 흠
        <hr />
      </div>

      {{ selected_movie }}asdasdasd
      <!-- <p>개요 : {{ movie.overview }}</p> -->
      <br />
      <br />
      <br />
      <br />
      <br />
      <!-- {{ movie.title }} -->
      <!-- {{ movie.title }} -->
    </section>
    <section class="border">
      <h1>글작성 2~3개 보여주고 더보기 -> 이 영화의 전체 커뮤니티</h1>
      <button @click="getMovieArticles(selected_movie)">게시글 불러오기</button>
      {{ articles }}
      <div class="overflow-auto container">
        <b-table :items="pageArticles" fixed :per-page="perPage" :current-page="currentPage" hover></b-table>
        <hr />
        <b-pagination
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="my-table"
          align="center"
        ></b-pagination>
      </div>
      <a href="#">더 보기</a>
    </section>

    <section class="border">
      <h1>장르나 비슷한 영화 추천하는 섹션</h1>
    </section>
  </div>
</template>

<script>
import axios from "axios";

// const API_KEY = process.env.VUE_APP_API_KEY_TMDB
const IMG_URL = "https://image.tmdb.org/t/p/w200";

export default {
  name: "MovieDetailView",
  props: {
    selected_movie: Object,
    articles: Array
  },
  data() {
    return {
      poster: null,
      
      perPage: 15,
      currentPage: 1,
    };
  },
  computed: {
    rows() {
      return this.articles.length;
    },
    pageArticles() {
      return this.articles.map((items) => {
        let user = items["user"].username
        console.log(user)
        
        return items
      })
    }
  },
  methods: {
    getMovieDetail() {
      axios
        .get(`${IMG_URL}${this.selected_movie.poster_path}`)
        .then(res => {
          console.log(res.config.url);
          this.poster = res.config.url;
          console.log(this.poster);
        })
        .catch(err => {
          console.log(err);
        });
    },
    getMovieArticles(movie) {
      this.$emit("submit-movie-for-articles", movie);
    }
  },
  created() {
    this.getMovieDetail()
    this.getMovieArticles(this.selected_movie);
    console.log(this.$route.params.id);
  }
};
</script>

<style>
.rr {
  margin-left: 250px;
}
img {
  margin: 0;
}
</style>