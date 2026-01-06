import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import Items from '../views/Items.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/items',
    name: 'Items',
    component: Items
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
