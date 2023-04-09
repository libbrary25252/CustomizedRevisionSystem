<template>
  <div class="section">
    <h1 class="title px-1">Login</h1>
    <p class=" is-size-5-mobile px-1 subtitle">
      Please log in to continue.
    </p>
    <br>
    <div class="container login">
      <form class="box loginBox" @submit.prevent="submitForm">
        <div class="field">
          <label class="label">User Name</label>
          <div class="control">
            <input class="input" type="text" placeholder="Username" v-model="username">
          </div>
        </div>

        <div class="field">
          <label class="label">Password</label>
          <div class="control">
            <input class="input" type="password" placeholder="********" v-model="password">
          </div>
        </div>

        <div class="field">
          <div class="control">
            <p class="is-size-7 pb-4">Forget Your <router-link
                to="/signup"><strong>Username/Password</strong>?</router-link></p>
            <div class="is-fullwidth has-text-centered pt-3">
              <button class="button is-primary loginBtn">Login</button>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginView',
  data() {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  components: {

  },
  methods: {
    async submitForm() {
      console.log("?")
      axios.defaults.headers.common["Authorization"] = ""
      localStorage.removeItem("token")
      const formData = {
        username: this.username,
        password: this.password
      }
      console.log(formData);
      await axios
        .post("/api/v1/token/login/", formData)
        .then(response => {
          const token = response.data.auth_token
          this.$store.commit('setToken', token)
          axios.defaults.headers.common["Authorization"] = "Token " + token
          localStorage.setItem("token", token)
          console.log("success?")
          window.location.href = '/home'
        })
        .catch(error => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`)
            }
          } else {
            this.errors.push('Something went wrong. Please try again')
            console.log(JSON.stringify(error))
          }
        })
    }
  }
}
</script>

<style>
@media (min-width:961px) {
  .login {
    max-width: 60% !important;
    padding-left: 32px;
    padding-right: 32px;
    width: 100%;
  }
}

@media screen and (max-width:641px) {

  /* portrait tablets, portrait iPad, landscape e-readers, landscape 800x480 or 854x480 phones */
  .login {
    max-width: none !important;
    padding-left: 32px;
    padding-right: 32px;
    width: 100%;
  }
}


.loginBtn {
  width: 100%;
}

.loginBox {
  padding: 2.5rem;
}
</style>