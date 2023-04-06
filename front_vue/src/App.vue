<template>
  <body>
    <div id="app">
      <nav class="navbar px-5" role="navigation" aria-label="main navigation">
        <div class="navbar-brand is-size-4">
          <router-link to="/home" class="navbar-item"><strong>Smart Campus</strong></router-link>

          <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar_menu"
            @click.prevent="this.showMobileMenu = !this.showMobileMenu;">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div id="navbar_menu" class="navbar-menu" v-bind:class="{ 'is-active': isMobile() }">
          <div class=" navbar-start">
            <router-link to="/home" class="navbar-item">
              Home
            </router-link>


            <div class="navbar-item has-dropdown" v-if="isLogin()" v-bind:class="{ 'is-active': isActive }" @click="show()">
              <a class="navbar-link">
                CRS
              </a>

              <div class="navbar-dropdown" :class="dropdownClasses">
                <router-link to="/createQList" class="navbar-item">
                  Search Question
                </router-link>
                <router-link to="/genQList" class="navbar-item">
                  Find Category
                </router-link>

                <hr class="navbar-divider">
                <router-link to="/report" class="navbar-item">
                  Report an issue
                </router-link>
              </div>
            </div>

            <router-link to="/activity" class="navbar-item" v-if="isLogin()">
              My History
            </router-link>
          </div>

          <div class="navbar-end">
            <div class="navbar-item">
              <div class="buttons">
                <router-link to="/profile" class="button is-info" v-if="isLogin()">
                  <strong>Profile</strong>
                </router-link>
                <router-link to="/login" class="button is-light" v-if="isLogin()==false">
                  Log in
                </router-link>
                <button class="button is-light" v-if="isLogin()" @click="logout">
                  Log out
                </button>
              </div>
            </div>
          </div>
        </div>
      </nav>


      <!-- <div>
<nav class="navbar is-dark">
  <div class="navbar-brand">
  <router-link to="/" class="navbar-item"><strong>Smart Campus</strong></router-link>
  <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar_menu" @click="showMobileMenu = !showMobileMenu">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
  </a>
  </div>

  <div class="navbar-menu" id="navbar_menu" v-bind:class="{'is-active': showMobileMenu}">
    <div class="navbar-start">
      <router-link to="/createQList" class="navbar-item">CRS</router-link>
      <router-link to="/report" class="navbar-item">Report</router-link>  need filter the user type 
      <router-link to="/activity" class="navbar-item">Activity</router-link>  need integrate with milk box
    </div>
    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
          <router-link to="/login" class="button is-light">Log in</router-link>
          <router-link to="/profile" class="button is-success">
            <span class="icon"><i class="fas fa-user"></i></span>
            <span>Profile</span>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</nav> -->


        <router-view />
      
      <footer class="footer">
        <p class="has-text-centered">Copyright (c) 2022</p>
      </footer>
    </div>
  </body>
</template>

<style>
body {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

#app {
  flex: 1;
  display: flex;
  flex-direction: column;
}

footer {
  margin-top: auto;
}
</style>

<script>
import { throwStatement } from '@babel/types';
import axios from 'axios';

export default {
  data() {
    return {
      showMobileMenu: false,
      isActive: false,
      isClick: false,
      needLogin: true
    }
  },
  beforeCreate() {
    this.$store.commit('initalizeStore');
    const token = this.$store.state.token;
    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token;
    }else {
      axios.defaults.headers.common['Authorization'] = "";
    }
  },
  computed: {
    dropdownClasses: function () {
      if (this.isActive) {
        return "is-active";
      } else {
        return "is-hidden";
      }
    }
  },
  methods: {
    show: function () {
      this.isActive = !this.isActive;
    },
    isMobile: function () {
      return this.showMobileMenu;
    },
    isLogin(){
      if(localStorage.getItem('token')) {
        return true;
      }else return false;
    },
    logout() {
      axios.post('/api/v1/token/logout/')
    .then(response => {
       const token = response.data.auth_token
          this.$store.commit('removeToken', token)
          axios.defaults.headers.common["Authorization"] = ""
          localStorage.removeItem('token');
          console.log("logout")
          window.location.href = '/login' // Redirect to login page
    })
    .catch(error => {
      // Handle the error
      if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`)
            }
          } else {
            this.errors.push('Something went wrong. Please try again')
            console.log(JSON.stringify(error))
          }
    }); 
    },
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
