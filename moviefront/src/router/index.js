import Vue from 'vue'
import VueRouter from 'vue-router'
import SignupView from '../views/accounts/SignupView.vue'
// import LoginView from '../views/accounts/LoginView.vue'
import ArticleCreateView from '../views/community/ArticleCreateView.vue'
import ArticleListView from '../views/community/ArticleListView.vue'
import MovieView from '../views/community/MovieView.vue'
import MovieDetailView from '../views/community/MovieDetailView.vue'
import MovieDataInsert from '../views/movie/MovieDataInsert.vue'
import FirstView from '../views/accounts/FirstView.vue'
import MovieRecommandView from '../views/movie/MovieRecommandView.vue'
import eachCommunityView from '../views/community/eachCommunityView.vue'
import ArticleDetail from '../views/community/ArticleDetail.vue'





Vue.use(VueRouter)

  const routes = [
  {
    path: '/movie/MovieDataInsert',
    name: 'MovieDataInsert',
    component: MovieDataInsert
  },
  {
    path: '/accounts/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/accounts/login',
    name: 'FirstView',
    component: FirstView
  },
  {
    path: '/community/create',
    name: 'ArticleCreateView',
    component: ArticleCreateView
  },
  {
    path: '/movie/id',
    name: 'ArticleListView',
    component: ArticleListView
  },
  {
    path: '/',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/movie/:movie',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/accounts/first',
    name: 'FirstView',
    component: FirstView
  },
  {
    path: '/recomand',
    name: 'MovieRecommandView',
    component: MovieRecommandView
  },
  {
    path: '/movie/artcles',
    name: 'eachCommunityView',
    component: eachCommunityView
  },
  {
    path: '/movie/:movie/article/:article',
    name: 'ArticleDetail',
    component: ArticleDetail
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
