<template>
  <div>
    <h1>게시글 목록</h1>
    <div class="overflow-auto container">
      <b-table :items="pageArticles" fixed :per-page="perPage" :current-page="currentPage" hover >
        
      </b-table>
      <hr>
      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="my-table"
        align="center"
      ></b-pagination>

    </div>
  </div>
</template>

<script>
import axios from "axios";

const BACK_URL = "http://127.0.0.1:8000";

export default {
  name: "ArticleListView",
  data() {
    return {
      articles: [],
      perPage: 15,
      currentPage: 1,
    };
  },
  computed: {
    rows() {
      return this.articles.length;
    },
    pageArticles() {
      return this.articles.map((items) => {
        let user = items["user"].username

        items["user"] = user
        return items
      })
    }
  },
  methods: {
    getArticles() {
      axios
        .get(`${BACK_URL}/community/`)
        .then(res => {
          this.articles = res.data;
        })
        .catch(err => {
          console.log(err.response.data);
        });
    }
  },
  created() {
    this.getArticles();
  }
};
</script>

<style>
</style>