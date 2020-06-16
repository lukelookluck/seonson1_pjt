<template>
  <div class="container">
    <h1>커뮤니티 - 수정 필요</h1>
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
      <div class="form-group">
        <label>영화id값</label>
        <input class="form-control" v-model="articleData.movie">
      </div>
      <button type="button" @click="create" class="btn btn-primary">작성하기</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "Create",
  data() {
    return {
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
      this.$emit("submit-article-data", this.articleData);
    }
  }
};
</script>

<style>
</style>