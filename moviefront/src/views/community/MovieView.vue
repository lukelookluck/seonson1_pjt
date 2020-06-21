<template>
  <div>
    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
      <div class="carousel-inner position-relative" >
        <div class="carousel-item active" data-interval="5000">
          <img src="../../../src/assets/a.jpg" class="d-block w-100" alt="..." />
        </div>
        <div class="carousel-item" data-interval="5000">
          <img src="../../../src/assets/b.jpg" class="d-block w-100" alt="..." />
        </div>
        <div class="carousel-item" data-interval="5000">
          <img src="../../../src/assets/c.jpg" class="d-block w-100" alt="..." />
        </div>
        <div class="carousel-item" data-interval="5000">
          <img src="../../../src/assets/d.jpg" class="d-block w-100" alt="..." />
        </div>
        <div class="carousel-item" data-interval="5000">
          <img src="../../../src/assets/e.jpg" class="d-block w-100" alt="..." />
        </div>
      </div>
    </div>
    <div class="container" id="main-container">
      <div id="title-movie-list" class="title-movie-list p-3 mb-3">
        <h1 class="text-black shadow   bg-white rounded mb-5 p-2">영화 평가하기</h1>
      </div>
      <!-- <button @click="getMovies">일단 눌러</button> -->
      <!-- {{list}} -->

      <div
        v-for="(movie, $idx) in list"
        :key="$idx"
        :movie="movie"
        class="card mx-auto mb-2"
        style="max-width: 65%;"
      >
        <div class="row no-gutters ">
          <div class="col-md-4">
            <a href="#" @click="detail(movie)">
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
              <!-- {{ movies[$idx].like }} -->

              <!-- {{ window.getElementById('movie.title') }}asdas -->
              <b-input-group>
                <b-form-rating
                  @change="rating(movie)"
                  v-model="movie.rate_value"
                  color="#ff8800"
                  size="lg"
                  no-border
                ></b-form-rating>

              </b-input-group>
              <!-- <p class="card-text">{{ movie.overview }}</p> -->
            </div>
          </div>
        </div>
      </div>

      <infinite-loading @infinite="infiniteHandler"></infinite-loading>
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
  </div>
</template>

<script>
import InfiniteLoading from "vue-infinite-loading";
import axios from "axios";

// const api = '//hn.algolia.com/api/v1/search_by_date?tags=story';
// import MovieDetailView from "./MovieDetailView.vue";
// import VideoListItem from './VideoListItem.vue'
// const API_KEY = process.env.VUE_APP_API_KEY_TMDB
const BACK_URL = "http://127.0.0.1:8000";

export default {
  name: "MovieView",
  props: {
    movies: Array
  },
  components: {
    InfiniteLoading
  },
  data() {
    return {
      movie2: this.movies,

      rateData: {
        user: null,
        movie: null,
        value: null
      },
      page: 0,
      list: []
    };
  },
  created() {
    console.log("asd");
    console.log("asdasd");
    if (this.$cookies.isKey("auth-token")) {
      this.isLogin = true;
    } else {
      this.$router.push("/accounts/login");
    }
  },
  methods: {
    infiniteHandler($state) {
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .get(`${BACK_URL}/movies/${this.page}/`, requestHeaders)
        .then(({ data }) => {
          console.log(data);
          if (data.length) {
            this.page += 1;
            this.list.push(...data);
            $state.loaded();
          } else {
            $state.complete();
          }
        });
    },
    detail(movie) {
      console.log(movie.id);
      this.$emit("submit-detail-movie", movie);
    },

    rating(rateValue) {
      this.rateData.movie = rateValue.id;
      this.rateData.value = rateValue.rate_value;
      this.$emit("submit-rate-value", this.rateData);
    }
  }
};
</script>

<style >
.title-movie-list {
  margin: auto;
  margin-top: 150px;
  width: 353px;
  /* background: white; */
}

#carouselExampleIndicators img {
  height: 650px;
}

#main-container {
  position: relative;
  bottom: 700px;
}
</style>