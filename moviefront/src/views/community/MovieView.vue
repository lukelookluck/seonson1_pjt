<template>
  <div class="container">
    <h1>영화 평가하기</h1>
    <!-- <button @click="getMovies">일단 눌러</button> -->
    <hr />
    <!-- {{ movies }} -->
    <!-- <div class="container">
      <ul v-for="movie in movies" :key="movie.id">
        <li>{{ movie.title }}</li>
      </ul>
    </div>-->
    <div v-for="movie in movies" :key="movie.id" class="card mx-auto" style="max-width: 50%;">
      <div class="row no-gutters">
        <div class="col-md-4">
          <a href>
            <img
              @click="detail(movie)"
              :src="'https://image.tmdb.org/t/p/original/'+ movie.poster_path"
              class="card-img"
              alt="..."
            />
          </a>
          <!-- {{ movies }} -->
        </div>
        <div class="col-md-8">
          <div class="card-body text-left">
            <h4 class="card-title">{{ movie.title }}</h4>
            <p class="card-text">
              <small class="text-muted">{{ movie.release_date.substring(0,4) }}</small>
            </p>
          <button @click="like(movie)" >조아요</button>

            <!-- {{ window.getElementById('movie.title') }}asdas -->
            <b-input-group>
              <b-form-rating @change="rating(movie)" v-model="movie.rate" color="#ff8800" size="lg" no-border>
              </b-form-rating>
              <!-- <b-input-group-append> -->
                <!-- <b-input-group-text
                  class="justify-content-center"
                  style="min-width: 3em;"
                >{{ value }}</b-input-group-text> -->
              <!-- </b-input-group-append> -->
            </b-input-group>
            <!-- <p class="card-text">{{ movie.overview }}</p> -->
          </div>
        </div>
      </div>
    </div>

    <!-- <div>
      <b-carousel
        id="carousel-fade"
        style="text-shadow: 0px 0px 2px #000"
        indicators
        img-width="300px"
        img-height="100px"
      >

        <b-carousel-slide v-for="movie in movies" :key="movie.id" :caption="movie.title" :img-src="'https://image.tmdb.org/t/p/original/'+ movie.poster_path">
          <button @click="detail(movie)">123</button>
        </b-carousel-slide>

        

      </b-carousel>
    </div>-->
  </div>
</template>

<script>
import axios from "axios";

// const API_KEY = process.env.VUE_APP_API_KEY_TMDB
const BACK_URL = "http://127.0.0.1:8000";


export default {
  name: "MovieView",
  data() {
    return {
      movies: [],
      selectedMovie: null,
      likeData: {
        id: null,
        like: null
      },
      newValue: null, 
      
    };
  },
  // computed: {
  //   release_year() {
  //     return 
  //     }
  // },

  created() {
    axios
      .get(`${BACK_URL}/movies/`)
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
    detail(movie) {
      console.log(movie.id);
      this.selectedMovie = movie;
      console.log(this.selectedMovie);
      // this.movie
      this.$router.push({
        name: "MovieDetailView",
        params: {
          id: movie.id,
          selectedMovie: movie
          // selectedMovie: x,
        }
      });
      // this.$router.push(`community/movie/${movie.id}`, movie)
    },
    like(movie) {
      this.likeData.id = movie.id;
      console.log(this.likeData);
      this.$emit("submit-like-movie", this.likeData);
    },
    rating(rateValue) {
      console.log(rateValue, rateValue.rate)

    }
    
  }
};
</script>

<style>
</style>