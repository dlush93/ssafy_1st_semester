import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginView from '@/views/accounts/LoginView.vue'
import SignupView from '@/views/accounts/SignupView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import ArticleListView from '@/views/articles/ArticleListView.vue'
import ArticleCreateView from '@/views/articles/ArticleCreateView.vue'
import ArticleDetailView from '@/views/articles/ArticleDetailView.vue'

Vue.use(VueRouter)

  const routes = [
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
    path: '/articles',
    name: 'ArticleListView',
    component: ArticleListView
  },
  {
    path: '/articles/create',
    name: 'ArticleCreateView',
    component: ArticleCreateView
  },
  {
    path: '/articles/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView
  },

  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const publicPages = ['ArticleListView', 'ArticleDetailView', 'LoginView', 'SignupView']  // Login 안해도 됨
  const authPages = ['LoginView', 'SignupView']  // Login 되어있으면 안됨
  
  const authRequired = !publicPages.includes(to.name)  // 로그인 해야 함.
  const unauthRequired = authPages.includes(to.name)  // 로그인 해서는 안됨
  const isLoggedIn = !!Vue.$cookies.isKey('auth-token')

  if(unauthRequired && isLoggedIn) {
    next('/articles')
  }
  authRequired && !isLoggedIn ? next({ name: 'LoginView'}) : next()
})

export default router
