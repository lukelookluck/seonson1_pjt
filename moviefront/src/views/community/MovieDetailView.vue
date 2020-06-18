<template>
  <div class="container" style="position: relative;">
    
    <img
      id="poster1"
      :src="'https://image.tmdb.org/t/p/original/'+ selected_movie.backdrop_path"
      alt="poster"
    />
    <img id="poster2" :src="'https://image.tmdb.org/t/p/w200/'+ selected_movie.poster_path" alt />
    <div id="title" style="position: relative;">
      <h1 class="text-white text-left">{{ selected_movie.title }}</h1>
      <h5 class="text-white text-left pl-3">
        {{ selected_movie.release_date.substring(0,4) }}
        <span
          v-for="genre in genres"
          :key="genre.db_id"
        >ㆍ{{ genre.name }}</span>
      </h5>
    </div>
    <div style="position: relative; top: -350px;">
      <section class="border">
        <div class="container">
          <b-input-group>
            <b-form-rating
              @change="rating(selected_movie)"
              no-border
              size="lg"
              v-model="selected_movie.rate_value"
              color="#ff8800"
            ></b-form-rating>
          </b-input-group>
        </div>
        <span></span>
        <b-button variant="outline-success" @click="like(selected_movie)" id="likebutton" size="sm" >
          조아요
          <b-badge variant="light">{{ newValue.a }}</b-badge>
        </b-button>

        <hr />
        <div class="text-left m-4">
          <h3 class="my-4">기본정보</h3>
          <span>{{ selected_movie.overview }}</span>
        </div>
      </section>
      <section class="border mt-3">
        <div class="overflow-auto container">
          <b-table
            :items="pageArticles"
            fixed
            :per-page="perPage"
            :current-page="currentPage"
            hover
          >
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
      </section>
    </div>
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
      selectMovie: null,
      newValue: {
        a: this.selected_movie.like.length,
        b: false
      },
      poster: null,
      poster2: null,
      genres: [],
      perPage: 3,
      currentPage: 1,
      rateData: {
        user: null,
        movie: null,
        // value: this.selected_movie.rated_movie[0].value
      },
      likeData: {
        id: null,
        like: null
      }
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
    goAticleForm() {
      this.$router.push("/community/create", {
        params: {
          id: this.selected_movie.id,
          selectedMovie: this.selected_movie
          // selectedMovie: x,
        }
      });
    },
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
    like(a) {
      console.log(a);
      this.likeData.id = a.id;
      if (this.newValue.b === false) {
        this.newValue.a++;
        this.newValue.b = true;
      } else {
        this.newValue.a--;
        this.newValue.b = false;
      }
      this.$emit("submit-like-movie", this.likeData);
    }
  }
};
</script>

<style scoped>
#poster1 {
  max-width: 100%;
}
#poster2 {
  max-width: 100%;
  position: relative;
  bottom: 330px;
  right: 410px;
}
#title {
  position: relative;
  bottom: 410px;
  right: -270px;
  font-size: 250%;
}
#likebutton {
  width: 45%;
}
</style>