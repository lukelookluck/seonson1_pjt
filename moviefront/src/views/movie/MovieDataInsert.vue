<template>
  <div>
    <!-- <button @click="insertMovieData">영화데이터db저장</button> -->
    <span>장르 저장에 3분, 영화 목록 20개당 3.5초 소요, 현재 2000개 저장으로 6분 소요, 총 9분 정도 소요됨</span>
    <button @click="insertGenreData">영화db저장 실행</button>
    <!-- <button @click="connectGenreMovie">영화랑 장르랑</button> -->
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
      genres: [],
      insertDataForMovie: {
        original_title: null,
        title: null,
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
      insertDataForGenre: {
        id: null,
        name: null,
        db_id: null,
      },
      my_sec: 1,
    }
  },  
  methods: {
    insertMovieData() {
      let my_sec = 0
      // my_sec x일 경우, 20*x 개
      while (my_sec < 1) {
        my_sec++
        setTimeout(() => {
          axios.get(BACK_URL_MOVIE_DATA, {
            params: {
              api_key: API_KEY,
                language: "ko-kr",
                page: this.count++,
            }
          })
          .then(res => {
              this.movies = res.data.results;
              console.log(this.movies)
              for (let movie in this.movies) {
                setTimeout(() => {
                  this.$emit("submit-movie-data", this.movies[movie])
                }, movie * 150);
              }
            })
          .catch(err => {
            console.log(err.data);
          });
        }, my_sec * 3500);

      }
    },
    insertGenreData() {
      
      axios.get(BACK_URL_GENRE_DATA, {
        params: {
          api_key: API_KEY,
            language: "ko",
        }
      })
      .then(res => {
        // console.log(res.data.genres)
        this.genres = res.data.genres
        for (let genre in this.genres) {
          setTimeout(() => {
            console.log("genre", this.genres[genre])
            this.insertDataForGenre.id = this.genres[genre].id
            this.insertDataForGenre.db_id = this.genres[genre].id
            this.insertDataForGenre.name = this.genres[genre].name
            console.log("insertDataForGenre", this.insertDataForGenre)
            this.$emit("submit-genre-data", this.insertDataForGenre)
            
          }, genre * 10000);
        }
      })
      .catch(err => {
        console.log(err)
      })
      
      setTimeout(() => {
        this.insertMovieData()
      }, 200000);

    },
    // connectGenreMovie() {
    //   for (let movie in this.movies) {
    //         setTimeout(() => {
    //           console.log("movie",this.movies[movie])
    //           this.insertDataForMovie.title = this.movies[movie].title
    //           this.insertDataForMovie.original_title = this.movies[movie].original_language
    //           this.insertDataForMovie.release_date = this.movies[movie].release_date
    //           this.insertDataForMovie.popularity = this.movies[movie].popularity
    //           this.insertDataForMovie.vote_count = this.movies[movie].vote_count
    //           this.insertDataForMovie.vote_average = this.movies[movie].vote_average
    //           this.insertDataForMovie.adult = this.movies[movie].adult
    //           this.insertDataForMovie.overview = this.movies[movie].overview
    //           this.insertDataForMovie.original_language = this.movies[movie].original_language
    //           this.insertDataForMovie.poster_path = this.movies[movie].poster_path
    //           this.insertDataForMovie.backdrop_path = this.movies[movie].backdrop_path
    //           this.insertDataForMovie.genres = this.movies[movie].genre_ids
    //           // this.insertData.like = this.movies[movie].like
    //           console.log("genres", this.movies[movie].genre_ids)
    //           console.log("genres",this.insertDataForMovie.genres)
    //           console.log("like", this.insertDataForMovie)
    //           // this.$emit("submit-movie-data", this.insertDataForMovie)
    //           this.$emit("connect-movie-genre", this.insertDataForMovie)
    //         }, movie * 10000);
    //       }
    // }
  }

}
</script>

<style>
</style>