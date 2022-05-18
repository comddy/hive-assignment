import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import moment from 'moment'
import * as echarts from 'echarts'

Vue.prototype.$echarts = echarts
var axios = require('axios')
axios.defaults.baseURL = 'http://localhost:5000'
Vue.prototype.$axios = axios
Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.prototype.$moment = moment
/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App),
  template: '<App/>',
  components: {App},
  router

}).$mount('#app')
