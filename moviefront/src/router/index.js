import Vue from 'vue'
import VueRouter from 'vue-router'
import SignupView from '../views/accounts/SignupView.vue'
import LoginView from '../views/accounts/LoginView.vue'
import ArticleCreateView from '../views/community/ArticleCreateView.vue'
import ArticleListView from '../views/community/ArticleListView.vue'
import MovieView from '../views/community/MovieView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/accounts/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/accounts/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/community/create',
    name: 'ArticleCreateView',
    component: ArticleCreateView
  },
  {
    path: '/',
    name: 'ArticleListView',
    component: ArticleListView
  },
  {
    path: '/community/movie',
    name: 'MovieView',
    component: MovieView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router