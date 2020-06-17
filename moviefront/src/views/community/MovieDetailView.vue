<template>
  <div class="container">
    <img class="d-flex" id="poster1" :src="poster" alt="poster" />
    <section class="border d-f">
      <img id="poster2" :src="'https://image.tmdb.org/t/p/w200/'+ selected_movie.poster_path" alt />
      <div id="title">
        <h1 class="text-white text-left">{{ selected_movie.title }}</h1>
        <h5 class="text-white text-left pl-3">
          {{ selected_movie.release_date.substring(0,4) }}
          <span
            v-for="genre in genres"
            :key="genre.db_id"
          >ㆍ{{ genre.name }}</span>
        </h5>
      </div>
      <hr />
      <div class="container">
        <b-input-group>
          <b-form-rating
            @change="rating(selected_movie)"
            no-border size="lg"
            v-model="selected_movie.rate_value"
            color="#ff8800"
          ></b-form-rating>
        </b-input-group>
      </div>
      <b-button variant="outline-success" @click="like(selected_movie)">조아요</b-button>

    </section>
    <section class="border">
      <div class="overflow-auto container">
        <b-table
          :items="pageArticles"
          fixed
          :per-page="perPage"
          :current-page="currentPage"
          v-for="article in pageArticles"
          :key="article.id"
          hover
        >
          <!-- <ul>
            <li v-for="n in 10" :key="n.id">{{ n }}</li>
          </ul>-->
          <template v-slot:cell(title)="data">
            <a href="#" @click="getArticle(selected_movie, data.item)">{{ data.item.title }}</a>
          </template>
        </b-table>
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
const IMG_URL = "https://image.tmdb.org/t/p/original";

export default {
  name: "MovieDetailView",
  props: {
    selected_movie: Object,
    articles: Array
  },
  data() {
    return {
      poster: null,
      poster2: null,
      genres: [],
      perPage: 3,
      currentPage: 1,
      rateData: {
        user: null,
        movie: null,
        value: this.selected_movie.rated_movie[0].value
      },
      likeData: {
        id: null,
        like: null
      },
    };
  },
  created() {
    this.getMovieDetail();
    this.getMovieArticles(this.selected_movie);
    console.log(this.$route.params.id);
    this.genres = this.selected_movie.genre_ids;
  },
  computed: {
    rows() {
      return this.articles.length;
    },
    pageArticles() {
      return this.articles.map(items => {
        let user = items["user"].username;
        console.log(user);

        return items;
      });
    }
  },
  methods: {
    getMovieDetail() {
      axios
        .get(`${IMG_URL}${this.selected_movie.backdrop_path}`)
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
    },
    getArticle(movie, article) {
      console.log("ASDASD", movie, article);
      this.$emit("show-article", movie, article);
    },
    rating(rateValue) {
    this.rateData.movie = rateValue.id;
    this.rateData.value = rateValue.rate_value;
    // console.log(this.rateData);
    this.$emit("submit-rate-value", this.rateData);
    },
    like(movie) {
      this.likeData.id = movie.id;
      this.newValue++
      this.$emit("submit-like-movie", this.likeData);
      
      
    },
  },
  
  
};
</script>

<style scoped>
#poster1 {
  margin: 0;
  width: 100%;
  max-width: 100%;
  height: 500px;
}
#poster2 {
  position: absolute;
  top: 300px;
  left: 420px;
}
#title {
  position: absolute;
  top: 500px;
  left: 650px;
  font-size: 250%;
}
</style>