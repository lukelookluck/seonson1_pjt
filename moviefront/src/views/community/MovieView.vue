<template>
  <div class="container">
    <h1>영화 리스트</h1>
    <button @click="getMovies">일단 눌러</button>
    <hr>
    <!-- <div class="container">
      <ul v-for="movie in movies" :key="movie.id">
        <li>{{ movie.title }}</li>
      </ul>
    </div> -->
    <div>
      <b-carousel
        id="carousel-fade"
        style="text-shadow: 0px 0px 2px #000"
        indicators
        img-width="300"
        img-height="100"
      >

        <b-carousel-slide v-for="movie in movies" :key="movie.id" :caption="movie.title" :img-src="'https://image.tmdb.org/t/p/original/'+ movie.backdrop_path">
          <button @click="detail(movie)">123</button>
          <button @click="like(movie)" >조아요</button>
        </b-carousel-slide>

        

      </b-carousel>
    </div>
  </div>
</template>

<script>
import axios from "axios"


const API_KEY = process.env.VUE_APP_API_KEY_TMDB
const BACK_URL = "https://api.themoviedb.org/3/movie/popular"

export default {
  name: "MovieView",
  data() {
    return {
      movies: [],
      selectedMovie: null,
      likeData: {
        like_movie: null,
      }
    };
  },
  methods: {
    getMovies() {
      // console.log(API_KEY);
      axios
        .get(BACK_URL, {
          params: {
            api_key: API_KEY,
            language: "ko",
            page: "1"
          }
        })
        .then(res => {
          this.movies = res.data.results;
          console.log(this.movies);
          // console.log(res.data.results);
          console.log(res.data.results);
        })
        .catch(err => {
          console.log(err.data);
        });
    },
    detail(movie){
      // console.log(movie.id)
      this.selectedMovie = movie
      // console.log(this.selectedMovie)
      // this.movie
      this.$router.push({
        name: 'MovieDetailView',
        params: {
          id: movie.id,
          selectedMovie: movie
          // selectedMovie: x,
        }
      })
      // this.$router.push(`community/movie/${movie.id}`, movie)
    },

    like(movie) {
      console.log(movie.id)
      this.likeData.like_movie = movie.id
      this.$emit("submit-like-movie", this.likeData)
    }
  }
}
</script>

<style>
</style>