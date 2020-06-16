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
    <div v-for="(movie, idx) in movie2" :key="movie.id" :movie="movie" class="card mx-auto" style="max-width: 50%;">
      <div class="row no-gutters">
        <div class="col-md-4">
          <a  href="#" @click="detail(movie)"  >
            <img
              
              :src="'https://image.tmdb.org/t/p/original/'+ movie.poster_path"
              class="card-img"
              alt="..."
            />
          </a>
          <!-- {{ movie }} -->
        </div>
        <div class="col-md-8">
          <div class="card-body text-left">
            <h4 class="card-title">{{ movie.title }}</h4>
            <p class="card-text">
              <small class="text-muted">{{ movie.release_date.substring(0,4) }}</small>
            </p>
            {{ movies[idx].like }}
          <button @click="like(movie)" >조아요</button>


            <!-- {{ window.getElementById('movie.title') }}asdas -->
            <b-input-group>
              <b-form-rating @change="rating(movie)" v-model="movie.rate_value" color="#ff8800" size="lg" no-border>
              </b-form-rating>
              <b-input-group-append>
                <b-input-group-text>{{ movie.rate_value }}</b-input-group-text>
              </b-input-group-append>
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
    </div> -->
  </div>
</template>

<script>
// import MovieDetailView from "./MovieDetailView.vue";
// import VideoListItem from './VideoListItem.vue'
// const API_KEY = process.env.VUE_APP_API_KEY_TMDB
// const BACK_URL = "http://127.0.0.1:8000";


export default {
  name: "MovieView",
  props: {
    movies: Array,
  },
  data() {
    return {
      movie2: this.movies,
      likeData: {
        id: null,
        like: null
      },
      rateData: {
        user: null,
        movie: null,
        value: null,
      }
      
    };
  },
  // components: {
  //   MovieDetailView,
  // },
  // computed: {
  //   release_year() {
  //     return 
  //     }
  // },

  created() {
    
  },
  methods: {
    detail(movie){
      console.log(movie.id)
      this.$emit("submit-detail-movie", movie);
      // axios.get(`${BACK_URL}/movies/${movie.id}`)
      // .then(res => {
      //   console.log(res.data)
      // })
      // .catch(err => {
      //   console.log(err.data)
      // })

    },
    like(movie) {
      this.likeData.id = movie.id;
      this.newValue++
      this.$emit("submit-like-movie", this.likeData);
      
      
    },
    rating(rateValue) {
      this.rateData.movie = rateValue.id
      this.rateData.value = rateValue.rate_value
      this.$emit('submit-rate-value', this.rateData)

    }
    
  }
};
</script>

<style>
</style>