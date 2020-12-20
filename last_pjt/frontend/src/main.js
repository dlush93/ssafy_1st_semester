import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueCookies from 'vue-cookies'
import StarRating from 'vue-star-rating'
import vueMoment from 'vue-moment'
import VueLodash from 'vue-lodash'
import lodash from 'lodash'

Vue.use(vueMoment)
// Vue.use(VueMomentJS, moment)
Vue.use(VueCookies)
Vue.use(VueLodash, { name: 'custom' , lodash: lodash })
Vue.config.productionTip = false
Vue.component('star-rating', StarRating);

new Vue({
  router,
  render: h => h(App),
  components: {
    StarRating
  }
}).$mount('#app')
