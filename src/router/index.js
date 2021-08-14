import { createRouter, createWebHashHistory } from 'vue-router'
import LogQuery from '@/components/LogQuery.vue'
import Home from '@/view/Home.vue'
import Welcome from '@/view/Welcome.vue'

const routes = [
  { // 重定向到主页
    path: '/', redirect: '/home'
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
    redirect: '/welcome',
    children: [
      { path: '/welcome', component: Welcome },
      { path: '/lq', component: LogQuery }
    ]
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
