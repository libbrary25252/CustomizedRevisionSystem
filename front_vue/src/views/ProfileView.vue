<template>
  <div class="section">
    <div class="card">
      <header class="card-header">
        <p class="card-header-title is-size-4">
          User Profile
        </p>
        <button class="card-header-icon" aria-label="more options">
          <span class="icon">
            <i class="fas fa-angle-down" aria-hidden="true"></i>
          </span>
        </button>
      </header>
      <div class="card-content">
        <div class="content">
          <div class="field">
            <label class="label">Role</label>
            <div class="control">
              <input class="input" type="text" :value="role" readonly>
            </div>
          </div>
          <div class="field">
            <label class="label">First Name</label>
            <div class="control">
              <input class="input" type="text" :value="firstname" readonly>
            </div>
          </div>
          <div class="field">
            <label class="label">Last Name</label>
            <div class="control">
              <input class="input" type="text" :value="lastname" readonly>
            </div>
          </div>
          <div class="field">
            <label class="label">Email</label>
            <div class="control">
              <input class="input" type="email" :value="email" readonly>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios';
export default {
  name: 'profile',
  data() {
    return {
      role: '',
      firstname: '',
      lastname: '',
      email: ''
    }
  },
  mounted() {
    this.fetchedData();
  },
  components: {

  },
  methods: {
    async fetchedData() {
      const token = localStorage.getItem('token');
      console.log(token)

      await axios.post(`/CRS/users/`, { 'token': token }).then(response => {
        console.log(response.data)
        const data = response.data;
        const role = data.role_id
        if (role == 1) {
          this.role = 'Teacher';
        } else if (role == 2) {
          this.role = 'Student';
        }
        const info = data.info_id;
        this.firstname = info.first_name;
        this.lastname = info.last_name;
        this.email = info.email;
      }).catch(error => console.log(error));
    },
    getInfo(data) {

    }
  },
}
</script>
  