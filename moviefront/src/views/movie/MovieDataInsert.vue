<template>
  <div>
    <button @click="insertMovieData">영화데이터db저장</button>
    <button @click="insertGenreData">장르데이터db저장</button>
  </div>
</template>

<script>
import axios from "axios"


const API_KEY = process.env.VUE_APP_API_KEY_TMDB
const BACK_URL_MOVIE_DATA = "https://api.themoviedb.org/3/movie/popular"
const BACK_URL_GENRE_DATA = "https://api.themoviedb.org/3/genre/movie/list"


export default {
  name: 'MovieDataInsert',
  data() {
    return {
      movies: [],
      insertData: {
        title: null,
        original_title: null,
        release_date: null,
        popularity: null,
        vote_count: null,
        vote_average: null,
        adult: null,
        overview: null,
        original_language: null,
        poster_path: null,
        backdrop_path: null,
        genres: null,
        like: null,
      },
      count: 1,
    }
  },
  methods: {
    insertMovieData() {
      axios.get(BACK_URL_MOVIE_DATA, {
        params: {
          api_key: API_KEY,
            language: "ko",
            page: this.count++,
        }
      })
      .then(res => {
          this.movies = res.data.results;
          for (let movie in this.movies) {
            setTimeout(() => {
              console.log("movie",this.movies[movie])
              this.insertData.title = this.movies[movie].title
              this.insertData.original_title = this.movies[movie].original_language
              this.insertData.release_date = this.movies[movie].release_date
              this.insertData.popularity = this.movies[movie].popularity
              this.insertData.vote_count = this.movies[movie].vote_count
              this.insertData.vote_average = this.movies[movie].vote_average
              this.insertData.adult = this.movies[movie].adult
              this.insertData.overview = this.movies[movie].overview
              this.insertData.original_language = this.movies[movie].original_language
              this.insertData.poster_path = this.movies[movie].poster_path
              this.insertData.backdrop_path = this.movies[movie].backdrop_path
              this.insertData.genres = this.movies[movie].genre_ids
              this.insertData.like = this.movies[movie].like
              // console.log("movie",this.movies[movie].genre_ids)
              console.log("insertData", this.insertData)
              // this.$emit("submit-movie-data", this.insertData)
                // this.$emit("submit-movie-data", this.movies[movie])
            }, movie * 7000);
          }
        })
      .catch(err => {
        console.log(err.data);
      });
    },
    insertGenreData() {
      axios.get(BACK_URL_GENRE_DATA, {
        params: {
          api_key: API_KEY,
            language: "ko",
        }
      })
      .then(res => {
        console.log(res.data.genres)
      })
      .catch(err => {
        console.log(err.data)
      })

    }
  }

}
</script>

<style>
</style>