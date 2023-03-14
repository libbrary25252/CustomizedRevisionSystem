import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/home',
    name: 'logo',
    component: HomeView
  },
  {
     // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    path: '/createQList',
    name: 'Question list',
    component: () => import('../views/CreateView.vue')
  },
  {
    path: '/genQList',
    name: 'Search Category',
    component: () => import('../views/GenView.vue')
  }, 
  {
    path: '/report',
    name: 'Report issue',
    component: () => import('../views/ReportView.vue')
  },
  {
    path: '/activity',
    name: 'Activity',
    component: () => import('../views/ActivityView.vue')
  },
  {
    path: '/profile',
    name: 'User Profile',
    component: () => import('../views/ProfileView.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/LoginView.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
