<template>
<div>
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
      <router-link to="/database" class="navbar-item">Database</router-link><!-- need filter the user type -->
      <router-link to="/activity" class="navbar-item">Activity</router-link><!-- need integrate with milk box-->
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
</nav>



  <section class="section">
    <router-view/>
  </section>

  <footer class="footer">
    <p class="has-text-centered">Copyright (c) 2022</p>
  </footer>
</div>
</template>

<script>
export default {
    data() {
      return {
        showMobileMenu: false,
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
