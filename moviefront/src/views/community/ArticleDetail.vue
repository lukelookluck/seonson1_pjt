<template>
  <div class="container">
    <section class="boader">
      <h1>article detail</h1>
      <!-- {{ selected_article }} -->
      {{ selected_article.title }}<br>
      {{ selected_article.content }}
    </section>
    <section class="boader">
      {{ comments }}
      <form class="text-left">
        <!-- <div class="form-group">
          <label>제목</label>
          <input
            class="form-control"
            aria-describedby="titleHelp"
            placeholder="제목"
            v-model="articleData.title"
          />
          <small id="titleHelp" class="form-text text-muted">영화와 관련된 자유로운 의견을 남겨주삼!!</small>
        </div> -->
        
        <div class="form-group">
          <label>내용</label>
          <textarea class="form-control" placeholder="내용" rows="5" v-model="commentData.content"></textarea>
        </div>
        <div class="form-group">
          <label>게시글id값</label>
          <input class="form-control" v-model="commentData.article">
        </div>
        <button type="button" @click="createComment" class="btn btn-primary">작성하기</button>
      </form>
    </section>
  
  </div>
</template>

<script>
export default {
    name: 'ArticleDetail',
    props: {
        selected_article: Object,
        comments: Array,
    },
    data() {
      return {
        commentData: {
          // user: null,
          article: null,
          content: null,
        }
      }
    },
    computed: {
      artcleComments() {
        return this.comments.map((items) => {
          let user = items["user"].username

          items["user"] = user
          return items
        })
      }
    },
    methods: {
      createComment() {
        this.$emit("submit-comment-data", this.commentData)
      }
    }
}
</script>

<style>

</style>