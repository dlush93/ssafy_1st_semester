import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginView from '@/views/accounts/LoginView.vue'
import SignupView from '@/views/accounts/SignupView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import MovieList from '@/views/movies/MovieView.vue'
import MovieDetail from '@/views/movies/MovieDetail.vue'
import CommunityView from '@/views/community/CommunityView.vue'

import UserProfileView from '@/views/accounts/profile/UserProfileView.vue'
import UserArticleList from '@/views/accounts/profile/UserArticleList.vue'
import UserLikeArticleList from '@/views/accounts/profile/UserLikeArticleList.vue'
import RankedMovieList from '@/views/accounts/profile/RankedMovieList.vue'

import ArticleDetail from '@/components/communitys/ArticleDetail.vue'
import ArticleList from '@/components/communitys/ArticleList.vue'
import axios from 'axios'
import cookies from 'vue-cookies'
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
      { path: '', name:'CommunityView', component: ArticleList },
      { path: 'detail',name:'ArticleDetail', component: ArticleDetail },
    ]
  },
  {
    path: '/accounts/:username',
    name: 'UserProfileView',
    component: UserProfileView,
    children : [
      { path : 'article', component: UserArticleList},
      {path : 'likearticle',  component : UserLikeArticleList},
      {path : 'rankedmovie', component : RankedMovieList}
    ],

    beforeEnter:(to,from,next)=>{
      const request_header = {
        headers: {
          'Authorization': `Token ${cookies.get('auth-token')}`
        }
      }
        if(cookies.isKey('auth-token')) {
          axios.post('http://127.0.0.1:8000/accounts/',null,request_header)
            .then((res)=> {
              if (res.data.username === to.params.username){
                next()
              } else{
                next('/')
              }
               
            })
        }
      

      console.log(from)
    }
  }
  

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
