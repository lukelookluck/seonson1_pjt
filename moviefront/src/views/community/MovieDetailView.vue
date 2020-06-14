<template>
  <div class="container">
      <section class="border">
        <h1>영화 정보 표시할 섹션</h1>
        <img class="d-flex" :src="poster" alt="poster">
        <div class="rr">
            <h1>{{ movie.title }}</h1>
            {{ movie.release_date }}, {{ movie.genre_ids }}
            장르 id를 db에 접근해서 비교해서 값을 가져와야하는데 흠 
            <hr>
        </div>
        {{ movie }}

        <p>개요 : {{ movie.overview }}</p>
        <br><br><br><br><br>
        <!-- {{ movie.title }} -->
        <!-- {{ movie.title }} -->
      </section>
      <section class="border">
        <h1>글작성 2~3개 보여주고 더보기 -> 이 영화의 전체 커뮤니티</h1>

        <a href="#">더 보기</a>
      </section>

      <section class="border">
        <h1>장르나 비슷한 영화 추천하는 섹션</h1>
      </section>
  </div>
</template>

<script>
import axios from "axios"

// const API_KEY = process.env.VUE_APP_API_KEY_TMDB
const IMG_URL = "https://image.tmdb.org/t/p/w200"

export default {
    name: 'MovieDetailView',
    // props: {
    //     movie: {
    //         type: Object,
    //     }
    // },
    data() {
        const movie = this.$route.params.selectedMovie
        return {
            movie,
            poster: null,
        }
    },
    methods: {
        getMovieDetail(){
            axios.get(`${IMG_URL}${this.movie.poster_path}`)
            .then(res => {
                console.log(res.config.url)
                this.poster = res.config.url
                console.log(this.poster)
            })
            .catch(err => {
                console.log(err)
            })
        },
    },
    created() {
        this.getMovieDetail()
        console.log(this.$route.params.id)
    }
}
</script>

<style>
.rr {
    margin-left: 250px;
}
img {
    margin: 0;
}
</style>