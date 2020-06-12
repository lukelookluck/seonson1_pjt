<template>
  <div>
      <section>
          <!-- <h1>아아아아</h1> -->
          {{ movie }}
          <br><br><br><br><br>
          <!-- {{ movie.title }} -->
          <!-- {{ movie.title }} -->
      </section>
      <!-- <img src="https://image.tmdb.org/t/p/original/{{ movie.poster_path }}" alt="poster"> -->
  </div>
</template>

<script>


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
            movie
        }
    }
}
</script>

<style>

</style>