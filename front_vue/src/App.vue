<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <router-link to="/home" class="navbar-item"><strong>Smart Campus</strong></router-link>

    <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar_menu" @click="showMobileMenu = !showMobileMenu">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div id="navbar_menu" class="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
    <div class="navbar-start">
      <router-link to="/home" class="navbar-item">
        Home
      </router-link>

      
      <div class="navbar-item has-dropdown is-hoverable dropdown-trigger  ">
        <a class="navbar-link">
          CRS
        </a>

        <div class="navbar-dropdown ">
          <router-link to="/createQList" class="navbar-item">
            Question List
          </router-link>
          <router-link to="/genQList" class="navbar-item">
            Search Category
          </router-link>

          <hr class="navbar-divider">
          <router-link to="/report" class="navbar-item">
            Report an issue
          </router-link>
        </div>
      </div>

      <router-link to="/activity" class="navbar-item">
        Activity
      </router-link>
    </div>

    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
          <router-link to="/profile" class="button is-primary">
            <strong>Profile</strong>
          </router-link>
          <router-link to="/login" class="button is-light">
            Log in
          </router-link>
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

  <section class="section">
    <router-view/>
  </section>
  <footer class="footer">
    <p class="has-text-centered">Copyright (c) 2022</p>
  </footer>
</template>

<script>
export default {
    data() {
      return {
        showMobileMenu: false,
        // isActive: false,
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
