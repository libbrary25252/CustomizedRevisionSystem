<template>
  <div class="genQ section">
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
        <button class="button is-danger is-rounded" @click="reset">Clear</button>
      </div>
      <div class="notification" id="Qcontainer_body">
        <form class="field" @submit.prevent="submitQuestion">
          <div class="box">
            <div class="Qcontainer_item block" v-bind:key="q" v-for="q, index in questionList">
              <br>
              <label class="label">
                Question {{ index + 1 }}: </label>
              <!-- <div class="level">
                <div class="level-left">
                  
                </div>
                <div class="level-right">
                  <button class="delete level-item" v-if="(index + 1) > 1" @click="removeList(index)"></button>
                </div> 
              </div> -->
              <div class="control">
                <textarea class="textarea" placeholder="Textarea" v-bind:class="{ 'is-danger': isvalidString() }"
                  v-model="q.text"></textarea>
              </div>
              <p class="help is-danger" v-if="isvalidString()">Inputted question is too short, it requires at least 10
                characters</p>
              <label class="label py-2">Topics: {{ q.result }}</label>
              <!-- <div class="notification is-danger" v-if="error.length">
                <p v-for="error in errors" v-bind:key="error">{{ }}</p>
              </div> -->
            </div>
            <div class="field Qbutton">
              <p class="control ">
                <button class="button is-link is-rounded" @click.prevent="submitQuestion(true)">
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
      SuccessResponse: false,
      InvalidString: false,
    }
  },
  methods: {
    addQuestion() {
      this.questionList.push({ 'text': '', 'result': '' })
    },
    reset() {
      this.questionList = [{ 'text': '', 'result': '' }];
      this.InvalidString = false;
    },
    isSuccess() {
      return this.SuccessResponse;
    },
    isvalidString() {
      return this.InvalidString;
    },
    close: function (event) {
      this.SuccessResponse = false;
    },
    async submitQuestion(isBtn = false) {
      this.InvalidString = false;
      if (this.SuccessResponse) {
        const elem = this.$refs.closeBtn;
        elem.click();
      }

      for (let i = 0; i < this.questionList.length; i++) {
        const question = this.questionList[i];
        // console.log(question.text.length)
        if (question.text.length >= 10) {
          await axios.post('/modelapi/api', { 'text': question.text })
            .then(response => {
              const topics = response.data["prediction"].join(", ");
              question.result = topics || "No result";
              console.log(question.result)
              this.SuccessResponse = true;
            }).then(response => {
              axios.post('/CRS/inputs/', {
                'index': i + 1,
                'uid': this.uid,
                'text': question.text,
                'result': question.result
              })
                .catch(error => {
                  console.log(error);
                });
            })
            .catch(error => {
              console.log(error);
              question.result = "Error";
            });
        } else {
          if (isBtn) this.InvalidString = true
        }
      }
    }
  }
}
</script>
  