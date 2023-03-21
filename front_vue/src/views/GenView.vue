<template>
  <div class="genQ">
    <p class="title  is-size-4-mobile mt-1">
      Generate Category with Inputted Question
    </p>
    <p class=" is-size-5-mobile subtitle">
      Input your questions that you want to know their corresponding <strong>topics</strong>.
    </p>
    <button class="button is-primary is-rounded mb-3" @click="addQuestion">
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
              <label class="label">Topics: {{ q.result }}</label>
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
      questionList: [] = [{ 'text': '', 'result': '' }],
      uid: 'st0001'
    }
  },
  methods: {
    addQuestion() {
      this.questionList.push({ 'text': '', 'result': '' })
    },
    async submitQuestion() {
      // this.questionList.forEach((ele, index) =>
      //   this.formData.push({ 'index': index + 1, 'uid': this.uid, 'text': ele.text, 'result': '' }))

      // for (var i = 0; i < this.formData.length; i++) {
      //   console.log({ i })
      //   console.log(this.formData[i])

      //   await axios.post('http://127.0.0.1:8000/api/model/', { 'text': this.formData[i].text }).then(response => {
      //     console.log(response.data);
      //     console.log(response.data["prediction"].join(", "));
      //     response.data["prediction"].length > 0 ? this.formData[i].result = response.data["prediction"].join(", ") : this.formData[i].result = "No result"
      //     console.log(this.formData[i]);
      //   })
      //     .catch(error => {
      //       console.log(error);
      //     })
      //     .then(response => {
      //       axios.post('http://127.0.0.1:8000/CRS/inputs', this.formData[i]).then(response => {
      //         console.log(response.data);
      //       })
      //         .catch(error => {
      //           console.log(error);
      //         });
      //     });
      // }
      // // reset the array
      // this.formData = [];
      for (let i = 0; i < this.questionList.length; i++) {
        const question = this.questionList[i];

        await axios.post('http://127.0.0.1:8000/api/model/', { 'text': question.text })
          .then(response => {
            const topics = response.data["prediction"].join(", ");
            question.result = topics || "No result";
            console.log(question.result)
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
  