<template>
    <div class="section">
        <h1 class="title px-1">Sign in</h1>
        <p class=" is-size-5-mobile px-1 subtitle">
            Please sign in to continue.
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
                    <label class="label">First Name</label>
                    <div class="control">
                        <input class="input" type="text" placeholder="First Name" v-model="firstname">
                    </div>
                </div>

                <div class="field">
                    <label class="label">Last Name</label>
                    <div class="control">
                        <input class="input" type="text" placeholder="Last Name" v-model="lastname">
                    </div>
                </div>

                <div class="field">
                    <label class="label">Phone Number</label>
                    <div class="control">
                        <input class="input" type="tel" v-model="phoneno" placeholder="+852-12345678" pattern="[0-9]{8}">
                    </div>
                </div>

                <div class="field">
                    <label class="label">Email</label>
                    <div class="control">
                        <input class="input" type="email" placeholder="abc@example.com" v-model="email">
                    </div>
                </div>

                <div class="field">
                    <label class="label">Password</label>
                    <div class="control">
                        <input class="input" type="password" placeholder="********" v-model="password">
                    </div>
                </div>

                <div class="field">
                    <label>Repeat password</label>
                    <div class="control">
                        <input type="password" class="input" v-model="password2">
                    </div>
                </div>

                <div class="field">
                    <div class="control">
                        <div class="is-fullwidth has-text-centered pt-3">
                            <button class="button is-primary loginBtn">Sign in</button>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'SignUp',
    data() {
        return {
            username: '',
            password: '',
            firstname: '',
            lastname: '',
            phoneno: '',
            email: '',
            password2: '',
            errors: []
        }
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.username === '') {
                this.errors.push('The username is missing')
            }

            if (this.password === '') {
                this.errors.push('The password is too short')
            }

            if (this.password !== this.password2) {
                this.errors.push('The passwords doesn\'t match')
            }

            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }

                axios
                    .post("/api/v1/users/", formData)
                    .then(response => {
                        toast({
                            message: 'Account created, please log in!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        this.$router.push('/log-in')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')

                            console.log(JSON.stringify(error))
                        }
                    })
            }
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

@media screen and (max-width:641px) { /* portrait tablets, portrait iPad, landscape e-readers, landscape 800x480 or 854x480 phones */ 
  .login {
    max-width: none !important;
    padding-left: 32px;
    padding-right: 32px;
    width: 100%;
  }
}


.loginBtn{
  width: 100%;
}

.loginBox {
  padding: 2.5rem;
}
</style>