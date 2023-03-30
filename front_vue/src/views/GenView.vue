<template>
  <div class="genQ">
    <div class="notification is-primary is-light" v-if="isSuccess()">
      <button class="delete" @click="close" ref="closeBtn"></button>
      Successfully generated the results!
    </div>
    <p class="title is-size-4-mobile mt-1">
      Find Category with Inputted Question
    </p>
    <p class=" is-size-5-mobile subtitle">
      Input the questions that you want to know their corresponding <strong>topics</strong>.
    </p>
    <div class="container is-max-desktop" id="QContainer">
      <div class="buttons  is-right">
        <button class="button is-primary is-rounded" @click="addQuestion">
          Add Question
        </button>
        <button class="button is-rounded is-danger">Export</button>
      </div>
      <div class="notification" id="Qcontainer_body">
        <form class="field" @submit.prevent="submitForm">
          <div class="box">
            <div class="Qcontainer_item block" v-bind:key="q" v-for="q, index in questionList">
              <br>
              <label class="label">Question {{ index + 1 }}: </label>
              <div class="control">
                <textarea class="textarea" placeholder="Textarea" v-model="q.text"></textarea>
              </div>
              <label class="label py-2">Topics: {{ q.result }}</label>
              <!-- <div class="notification is-danger" v-if="error.length">
                <p v-for="error in errors" v-bind:key="error">{{ }}</p>
              </div> -->
            </div>
            <div class="field Qbutton">
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
      questionList: [] = [{ 'text': '', 'result': '' }],
      uid: 'st0001',
      SuccessResponse: false
    }
  },
  methods: {
    addQuestion() {
      this.questionList.push({ 'text': '', 'result': '' })
    },
    isSuccess() {
      return this.SuccessResponse;
    },
    close: function (event) {
      this.SuccessResponse = false;
    },
    async submitQuestion() {

      if (this.SuccessResponse) {
        console.log("closed!")
        const elem = this.$refs.closeBtn;
        elem.click();
      }

      for (let i = 0; i < this.questionList.length; i++) {
        const question = this.questionList[i];

        await axios.post('http://127.0.0.1:8000/api/model/', { 'text': question.text })
          .then(response => {
            const topics = response.data["prediction"].join(", ");
            question.result = topics || "No result";
            console.log(question.result)
            this.SuccessResponse = true;
          })
          .catch(error => {
            console.log(error);
            question.result = "Error";
          }).then(response => {
            axios.post('http://127.0.0.1:8000/CRS/inputs', {
              'index': i + 1,
              'uid': this.uid,
              'text': question.text,
              'result': question.result
            })
              .then(response => {
                console.log(response.data);
              })
              .catch(error => {
                console.log(error);
              });
          });
      }
    }
  }
}
</script>
  