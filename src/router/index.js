import { createRouter, createWebHashHistory } from 'vue-router'
import LogQuery from '@/components/LogQuery.vue'
import Home from '@/view/Home.vue'

const routes = [
  { // 重定向到主页
    path: '/', redirect: '/home'
  },
  {
    path: '/lq',
    name: 'LogQuery',
    component: LogQuery
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
