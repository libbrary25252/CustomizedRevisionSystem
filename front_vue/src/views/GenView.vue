<template>
  <div class="genQ">
    <p class="title  is-size-4-mobile mt-1">
      Generate Category with Inputted Question
    </p>
    <p class=" is-size-5-mobile subtitle">
      Input your questions that you want to know their corresponding <strong>topics</strong>.
    </p>
    <button class="button is-primary is-rounded" @click="addQuestion">
      Add Question
    </button>
    <div class="container is-max-desktop" id="QContainer">
      <div class="notification" id="Qcontainer_body">
        <form class="field" @submit.prevent="submitForm">
          <div class="box">
            <div class="Qcontainer_item" v-bind:key="q" v-for="q, index in questionList">
              <br>
              <label class="label">Question {{ index + 1 }}: </label>
              <div class="control">
                <textarea class="textarea" placeholder="Textarea" v-model="q.text"></textarea>
              </div>
              <label class="label">Topics: {{}}</label>
              <!-- <div class="notification is-danger" v-if="error.length">
                <p v-for="error in errors" v-bind:key="error">{{ }}</p>
              </div> -->
            </div>
            <div class="field is-grouped Qbutton">
              <p class="control ">
                <button class="button is-link is-rounded" @click="submitQuestion">
                  Get Result
                </button>
              </p>
            </div>
          </div>
        </form>
      </div>
    </div>

  </div>
</template>

<style>
#Qcontainer_body {
  background-color: white;
}

#Qcontainer_body {
  background-color: rgb(227, 242, 253);
}

.control {
  margin-top: 2ch;
}
</style>
  
<script>
import axios from 'axios';

export default {
  name: 'GenView',
  data() {
    return {
      questionList: [] = [{ 'text': '' }],
      formData: [] = [],
      uid: 'st0001'
    }
  },
  methods: {
    addQuestion() {
      this.questionList.push({ 'text': '' })
    },
    async submitQuestion() {
      this.questionList.forEach(ele =>
        this.formData.push({ 'uid': this.uid, 'text': ele.text, 'result': '' }))

      for (var i = 0; i < this.formData.length; i++) {
        console.log({ i })
        console.log(this.formData[i].uid)
        await axios.post('http://127.0.0.1:8000/CRS/inputs', this.formData[i]).then(response => {
          console.log(response.data);
        })
          .catch(error => {
            console.log(error);
          });
      }
    }
  }
}
</script>
  