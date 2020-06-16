<template>
  <div class="container" >
    <h1>취향분석 - 무한 스크롤 구현 필요할까..</h1>
    <button @click="recomand">취향분석</button>
    <button @click="recomand2">비슷한 취향인 사람은 이걸 봤어요</button>
    
    <div v-for="(movie, idx) in recomand_movies" :key="movie.id" :recomand_movies="recomand_movies" class="card mx-auto" style="max-width: 50%;">
      <div class="row no-gutters">
        <div class="col-md-4">
          <a  href="#" @click="detail(movie)">
            <img
              
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
            {{ recomand_movies[idx].like }}
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

    <div v-for="(movie, idx) in recomand_movies2" :key="movie.id" :recomand_movies2="recomand_movies2" class="card mx-auto" style="max-width: 50%;">
      <div class="row no-gutters">
        <div class="col-md-4">
          <a  href="#" @click="detail(movie)">
            <img
              
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
            {{ recomand_movies2[idx].like }}
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




  </div>
</template>

<script>
export default {
  name: 'MovieRecommandView',
  props: {
    recomand_movies: Array,
    recomand_movies2: Array,
  },
  methods: {
    recomand() {
      this.$emit('submit-recomand-request')
    },
    recomand2() {
      this.$emit('submit-recomand-request-2')
    },
  }

}
</script>

<style>

</style>