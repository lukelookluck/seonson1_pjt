<template>
  <div class="mb-5">
    <div class="container">
      <section class="boader mt-5">
        <hr />
        <div class="text-left">
          <div class="d-flex justify-content-between">
            <div>
              <h1>{{ selected_article.title }}</h1>
              <p>{{selected_movie.title}}ㆍ{{ selected_movie.release_date.substring(0,4) }}</p>
              <p>작성자: {{selected_article.uesrname}}</p>
              <span>점수: {{selected_user[0].value}}</span>
            </div>
            <img
              id="poster2"
              :src="'https://image.tmdb.org/t/p/w200/'+ selected_movie.poster_path"
              alt
            />
          </div>
          <span>{{ selected_article.content }}</span>
        </div>
      </section>
      <hr />
      <div class="boader text-left">
        <p>댓글 목록</p>
        <hr />
        <ul class="mb-5 text-left">
          <li
            class="text-decoration-none"
            v-for="comment in comments"
            :key="comment.id"
          >{{ comment.content }} by. {{ comment.uesrname }}</li>
        </ul>
        
      </div>
    </div>
    <div id="comment-form" class="px-5 text-left py-3">
      <h5>댓글 작성</h5>
      <b-form class="d-flex" @button="createComment" >
          <b-form-input 
            id="input-1"
            type="text"
            class="m-0 mb-2 mr-sm-2 mb-sm-0 ml-1"
            placeholder="댓글쓰기"
            required
            v-model="content2"
            style="width: 860px;"
          ></b-form-input>
        <b-button type="submit" variant="success" class="text-sm" style="height: 38px;" @click="createComment" >작성</b-button> 
      </b-form>
    </div>
  </div>
</template>

<script>
export default {
  name: "ArticleDetail",
  props: {
    username: String,
    selected_movie: Object,
    selected_article: Object,
    comments: Array,
    selected_user: Object
  },
  data() {
    return {
      content2: '',
      articleComments: this.comments,
      commentData: {
        movie: this.selected_movie.id,
        article: this.selected_article.id,
        content: "",
        uesrname: this.username
      }
    };
  },
  computed: {
    artcleComments() {
      return this.comments.map(items => {
        let user = items["user"].username;

        items["user"] = user;
        return items;
      });
    }
  },
  methods: {
    createComment() {
      this.commentData.content = this.content2
      console.log(this.commentData)
      this.$emit("submit-comment-data", this.commentData);
      this.content2 = null
    }
  }
};
</script>

<style>
#comment-form {
  position: fixed;
  /* width: 100%; */
  margin: auto;
  padding: auto;
  bottom: 0px;
  background-color: white;
}
</style>
