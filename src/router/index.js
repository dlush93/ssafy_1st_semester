import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginView from '@/views/accounts/LoginView.vue'
import SignupView from '@/views/accounts/SignupView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import UserProfileView from '@/views/accounts/UserProfileView.vue'
import MovieList from '@/views/movies/MovieView.vue'
import MovieDetail from '@/views/movies/MovieDetail.vue'
import CommunityView from '@/views/community/CommunityView.vue'

import ArticleDetail from '@/components/communitys/ArticleDetail.vue'
import ArticleList from '@/components/communitys/ArticleList.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'MovieList',
    component: MovieList
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/logout',
    name: 'LogoutView',
    component: LogoutView
  },
  {
    path: '/moive/:id',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView,
    children: [
      { path: '', component: ArticleList },
      { path: 'detail', component: ArticleDetail },
    ]
  },
  {
    path: '/moive/:username',
    name: 'UserProfileView',
    component: UserProfileView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const publicPages = ['MovieList', 'LoginView', 'SignupView', 'MovieDetail', 'CommunityView', 'CommunityDetailView']  // Login 안해도 됨
  const authPages = ['LoginView', 'SignupView']  // Login 되어있으면 안됨
  
  const authRequired = !publicPages.includes(to.name)  // 로그인 해야 함.
  const unauthRequired = authPages.includes(to.name)  // 로그인 해서는 안됨
  const isLoggedIn = !!Vue.$cookies.isKey('auth-token')

  if(unauthRequired && isLoggedIn) {
    next('/')
  }
  if (authRequired && !isLoggedIn) {
    next({ name: 'LoginView'})
  } else {
    next()
  }

})

export default router
