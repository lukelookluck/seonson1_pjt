<template>
  <div class="container">
    <h2 class="text-success">칠면조 추천 작품</h2>
    <button
      @click="recomand2"
      class="btn btn-primary"
      data-toggle="modal"
      data-target="#exampleModal"
    >비슷한 취향인 사람은 이걸 봤어요</button>

    <div
      v-for="movie in list"
      :key="movie.id"
      :recomand_movies="recomand_movies"
      class="card mx-auto"
      style="max-width: 65%;"
    >
      <div class="row no-gutters">
        <div class="col-md-4">
          <a href="#" @click="detail(movie)">
            <img
              :src="'https://image.tmdb.org/t/p/original/'+ movie.poster_path"
              class="card-img"
              alt="..."
            />
          </a>
        </div>
        <div class="col-md-8">
          <div class="card-body text-left">
            <h4 class="card-title">{{ movie.title }}</h4>
            <p class="card-text">
              <small class="text-muted">{{ movie.release_date.substring(0,4) }}</small>
            </p>

            <b-input-group>
              <b-form-rating
                @change="rating(movie)"
                v-model="movie.rate_value"
                color="#ff8800"
                size="lg"
                no-border
              ></b-form-rating>
            </b-input-group>
          </div>
        </div>
      </div>
    </div>

    <infinite-loading @infinite="infiniteHandler"></infinite-loading>


    <div
      class="hidden modal fade"
      id="exampleModal"
      role="dialog"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
      data-backdrop="false"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">취향이 비슷한 사람이 본 영화</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div
              v-for="movie in recomand_movies2"
              :key="movie.id"
              :recomand_movies2="recomand_movies2"
              class="card mx-auto"
              style="max-width: 100%;"
            >
              <div class="row no-gutters">
                <div class="col-md-4">
                  <a href="#" @click="detail(movie)">
                    <img
                      :src="'https://image.tmdb.org/t/p/original/'+ movie.poster_path"
                      class="card-img"
                      alt="..."
                    />
                  </a>
                </div>
                <div class="col-md-8">
                  <div class="card-body text-left">
                    <h4 class="card-title">{{ movie.title }}</h4>
                    <p class="card-text">
                      <small class="text-muted">{{ movie.release_date.substring(0,4) }}</small>
                    </p>
                    <b-input-group>
                      <b-form-rating
                        @change="rating(movie)"
                        v-model="movie.rate_value"
                        color="#ff8800"
                        size="lg"
                        no-border
                      ></b-form-rating>
                    </b-input-group>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import InfiniteLoading from 'vue-infinite-loading';
import axios from 'axios';

// const api = '//hn.algolia.com/api/v1/search_by_date?tags=story';
const BACK_URL = "http://127.0.0.1:8000";


export default {
  name: "MovieRecommandView",
  
  props: {
    recomand_movies: Array,
    recomand_movies2: Array
  },
  components: {
    InfiniteLoading,
  },
  data() {
    return {
      rateData: {
        user: null,
        movie: null,
        value: null
      },
      page: 0 ,
      list: [],
    };
  },
  methods: {
    infiniteHandler($state) {
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios.get(`${BACK_URL}/movies/recomand/${this.page}/`, requestHeaders
      ).then(({ data }) => {
        console.log(data)
        if (data.length) {
          this.page += 1;
          this.list.push(...data);
          $state.loaded();
        } else {
          $state.complete();
        }
      });
    },
    recomand() {
      console.log("asd");
      this.$emit("submit-recomand-request");
    },
    recomand2() {
      this.$emit("submit-recomand-request-2");
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

<style>
</style>