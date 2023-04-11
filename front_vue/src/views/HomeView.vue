<template>
  <div>
    <section class="hero is-medium is-info">
      <div class="hero-body">
        <div class="container has-text-centered ">
          <p class="title is-size-2">
            Welcome to Smart Campus
          </p>
          <p class="subtitle is-size-4">
            Let's explore your customized study tour!
          </p>
        </div>
        <div class="container has-text-centered pt-6" v-if="isLogin() == false">
          <button class="button is-info is-light is-size-5" @click="gotoLogin">Sign in / Login</button>
        </div>
      </div>
    </section>
    <div class="home">
      <section class="section">
        <div class="container">
          <div class="has-text-centered pb-4" id="services-text-container">
            <h1 class="title is-2">What can you do here?</h1>
            <h4 class="subtitle">
              There are many functions you may explore.
            </h4>
          </div>
          <br />
          <div class="columns">
            <div class="column">
              <div class="card">
                <div class="card-content">
                  <!-- <div class="has-text-centered">
                    <img src="images/card-item-1.png" />
                  </div> -->
                  <h3 class="title is-3 has-text-centered" id="card-product-description">Search Question</h3>
                  <p class="has-text-centered">
                    You can search and generate a customized practice paper based on the types of question categories and
                    topics.
                  </p>
                </div>
              </div>
            </div>
            <div class="column">
              <div class="card">
                <div class="card-content">
                  <!-- <div class="has-text-centered">
                    <img src="images/card-item-1.png" />
                  </div> -->
                  <h3 class="title is-3 has-text-centered" id="card-product-description">Find Category</h3>
                  <p class="has-text-centered">
                    Are you confused about which category is belonging to your question? <br>If so, you can categories the
                    inputted question dataset into corresponding categories and topics here.
                  </p>
                </div>
              </div>
            </div>
            <div class="column">
              <div class="card">
                <div class="card-content">
                  <!-- <div class="has-text-centered">
                    <img src="images/card-item-1.png" />
                  </div> -->
                  <h3 class="title is-3 has-text-centered" id="card-product-description">Add Question</h3>
                  <p class="has-text-centered">
                    This function requires you to <strong>sign in first</strong>. <br>You can add questions to the
                    database.
                  </p>
                </div>
              </div>
            </div>
          </div>
          <!-- <div class="buttons is-centered">
          <button class="button is-black is-medium is-link">Read More</button>
        </div> -->
        </div>
      </section>
    </div>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'HomeView',
  data() {
    return {
    }
  },
  components: {

  },
  mounted() {
    this.fetchedData()
  },
  methods: {
    gotoLogin() {
      this.$router.push('/login');
    },
    isLogin() {
      if (localStorage.getItem('token')) {
        return true;
      } else return false;
    },
    async fetchedData() {
      const token = localStorage.getItem('token');
      console.log(token)

      await axios.post(`/CRS/users/`, { 'token': token }).then(response => {
        console.log(response.data)
        const data = response.data;
        const role = data.role_id
        localStorage.setItem('role', role)
        const info = data.info_id;
        localStorage.setItem('info_id', info.info_id)
      }).catch(error => console.log(error));
    },
  }
}
</script>
