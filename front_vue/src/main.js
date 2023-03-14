import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
// import Vue from 'vue'
// import VueSidebarMenu from 'vue-sidebar-menu'
// import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
axios.defaults.baseURL = "http://localhost:8080/home"
createApp(App).use(store).use(router, axios).mount('#app')
