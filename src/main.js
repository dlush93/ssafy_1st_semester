import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueCookies from 'vue-cookies'
import StarRating from 'vue-star-rating'

Vue.use(VueCookies)
Vue.config.productionTip = false
Vue.component('star-rating', StarRating);

new Vue({
  router,
  render: h => h(App),
  components: {
    StarRating
  }
}).$mount('#app')
