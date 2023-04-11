import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/home',
    name: 'logo',
    component: HomeView
  },
  {
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
    path: '/database',
    name: 'Database',
    component: () => import('../views/DatabaseView.vue')
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
  {
    path: '/signup',
    name: 'Sign Up',
    component: () => import('../views/SignupView.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
