import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import Spaetirun from '../views/Spaetirun.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/spaetirun',
    name: 'Spaetirun',
    component: Spaetirun
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
