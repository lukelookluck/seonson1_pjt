<template>
  <div class="container">
    <h1>{{ selected_movie.title }}에 대한 게시글 작성</h1>
    <form class="text-left">
      <div class="form-group">
        <label>제목</label>
        <input
          class="form-control"
          aria-describedby="titleHelp"
          placeholder="제목"
          v-model="articleData.title"
        />
        <small id="titleHelp" class="form-text text-muted">영화와 관련된 자유로운 의견을 남겨주삼!!</small>
      </div>
      <div class="form-group">
        <label>내용</label>
        <textarea class="form-control" placeholder="내용" rows="5" v-model="articleData.content"></textarea>
      </div>
      <button type="button" @click="create" class="btn btn-primary">작성하기</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "Create",
  props: {
    selected_movie: Object,
  },
  data() {
    return {
      selectMovie: this.selected_movie,
      articleData: {
        title: null,
        content: null,
        movie: null,
      }
    };
  },
  created() {
    if (!this.$cookies.isKey("auth-token")) {
      return this.$router.push("/");
    }
  },
  methods: {
    create() {
      console.log(this.selectMovie)
      this.articleData.movie = this.selectMovie.id
      console.log(this.articleData)
      this.$emit("submit-article-data", this.articleData);
    }
  }
};
</script>

<style>
</style>