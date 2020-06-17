<template>
<<<<<<< HEAD
  <div>
    <section class="boader mt-5">
      <!-- <h1>article detail</h1> -->
      <!-- {{ selected_movie.title }}<br> -->
=======
  <div class="container">
    <section class="boader">
      <h1>article detail</h1>
>>>>>>> f261b6f80cbc5f8f6fe479c4d81bdfd08175696e
      <!-- {{ selected_article }} -->
      게시글 제목 : {{ selected_article.title }}<br>
      게시글 내용 : {{ selected_article.content }}
    </section>
    <hr>
    <section class="boader">
      <p>댓글 목록</p><hr>
      <ul class="mb-5">
        <li v-for="comment in comments" :key="comment.id">
          {{ comment.content }} by. {{ comment.user }}
        </li>
      </ul>
      <!-- {{ comments }} -->
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
        
        <div class="form-group mb-5">
          <label>댓글 작성</label>
          <textarea class="form-control" placeholder="내용" rows="5" v-model="commentData.content"></textarea>
        </div>
        <!-- <div class="form-group">
          <label>게시글id값</label>
          <input class="form-control" v-model="commentData.article">
        </div> -->
        <button type="button" @click="createComment" class="btn btn-primary">작성하기</button>
      </form>
    </section>
  
  </div>
</template>

<script>
export default {
    name: 'ArticleDetail',
    props: {
        selected_movie: Object,
        selected_article: Object,
        comments: Array,
    },
    data() {
      return {
        // movie: null,
        // article: null,
        commentData: {
          // user: null,
          article: this.selected_article.id,
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
        // console.log(this.commentData.article_id)
        // console.log(this.commentData)
        this.$emit("submit-comment-data", this.commentData)
        // this.movie = this.selected_movie
        // this.article = this.selected_article
        // this.$router.push({
        //   name: "ArticleDetail",
        //   params: {
        //     id: this.article.id,
        //     // selectedMovie: x,
        //   }
        // })
      }
    }
}
</script>

<style>

</style>