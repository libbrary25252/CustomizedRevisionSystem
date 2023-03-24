<template>
  <div class="createQList">
    <div class="notification is-danger is-light" v-if="isEmpty()">
      <button class="delete" @click="close" ref="closeBtn"></button>
      Please choose the question type or topics before pushing the search button!
    </div>
    <p class="title is-size-4-mobile mt-1">
      Search From Database
    </p>
    <p class=" is-size-5-mobile subtitle">
      Search the questions from the database by selected categories.
    </p>
    <section class="container is-fullhd">
      <div class="box search_bar">
        <!-- <div class="field is-grouped">
          <p class="control is-expanded">
            <input class="input" type="text" placeholder="Find by keywords">
          </p>
          <p class="control">
            <a class="button is-link">
              Search
            </a>
          </p>
        </div> -->
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Question Type</label>
          </div>
          <div class="field-body">
            <div class="field">
              <label class="pr-2">
                <input type="checkbox" v-model="checkedTypes" value="MC">
                Multiple Choice
              </label>
              <label>
                <input type="checkbox" v-model="checkedTypes" value="LQ">
                Long Question
              </label>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Question Topics</label>
          </div>
          <div class="field-body">
            <div class="field is-normal">
              <div class="control select">
                <div class="select is-fullwidth is-multiple">
                  <select v-model="selectTopic" @change="setTopic(selectTopic)">
                    <option v-bind:key="i" v-for="i in topics" :value=i.value>{{ i.text }}</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="field is-horizontal">
          <div class="field-label">
            <label class="label">Selected Topics</label>
          </div>
          <div class="field-body">
            <div class="field is-normal is-flex-wrap-nowrap">
              <div class="tag pt-4 pb-5" id="tagwrapper" v-bind:key="i" v-for="i in TopicArr">
                <span class="tag is-info is-size-6"> {{ getName(i) }} <button class="delete is-small"
                    @click="removeTopic(i)"></button></span>
              </div>
            </div>
          </div>
        </div>
        <div class="pt-4 is-fullwidth has-text-centered">
          <button class="button is-link is-rounded block normal-btn" @click="search()">
            <span class="icon">
              <i class="fa fa-search" aria-hidden="true"></i>
            </span>
            <span>Search</span>
          </button>
        </div>
      </div>
    </section>
    <section class="pt-4 mt-6">
      <div class="result_box" v-bind:key="idx" v-for="idx in filtedList">
        <div class="result_container container">
          <div class="box result_box">{{ idx }}</div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'GenView',
  data() {
    return {
      selectTopic: '',
      checkedTypes: [],
      TopicArr: [],
      emptyError: false,
      QuestionList: [],
      filtedList: [],
      topics: [{ "text": "Algorithm Design", "value": "ALGO" }, { "text": "Basic Machine Organisation", "value": "BMO" }, { "text": "Computer System", "value": "COM" }, { "text": "Data Manipulation and Analysis", "value": "DM" }, { "text": "Data Organisation and Data Control", "value": "DO" }, { "text": "Elementary Web Authoring", "value": "ELEWEB" }, { "text": "Health and Ethical Issues", "value": "HEALTH" }, { "text": "Information Processing", "value": "INFO" }, { "text": "Intellectual Property", "value": "IP" }, { "text": "Internet Services and Applications", "value": "NETSEV" }, { "text": "Multimedia Elements", "value": "MEDIA" }, { "text": "Networking and Internet Basics", "value": "NETBAS" }, { "text": "Program Development", "value": "PROGRAM" }, { "text": "Spreadsheets and Databases", "value": "SD" }, { "text": "Threats and Security on the Internet", "value": "THREAT" }]
    }
  },
  components: {

  },
  methods: {
    setTopic: function (e) {
      this.TopicArr.push(e);
      // console.log(this.TopicArr);
      // console.log(this.selectTopic);
    },
    isEmpty() {
      return this.emptyError;
    },
    close: function (event) {
      this.emptyError = false;
    },
    getName: function (name) {
      for (var i = 0; i < this.topics.length; i++) {
        if (this.topics[i].value == name) {
          return this.topics[i].text;
        }
      }
    },
    removeTopic(val) {
      const idx = this.TopicArr.indexOf(val);
      if (idx > -1) {
        this.TopicArr.splice(idx, 1);
      }
      //console.log(this.TopicArr);
    },
    async search() {
      // console.log("checkedTypes: " + this.checkedTypes + " " + this.checkedTypes.length);
      // console.log("TopicArr: " + this.TopicArr + " " + this.TopicArr.length);
      if (this.checkedTypes.length == 0 && this.TopicArr.length == 0) {
        this.emptyError = true;
        // console.log("Empty error");
      } else {
        // const quest_form = { 'Qtype': this.checkedTypes.toString(), 'category': this.TopicArr.toString() };
        axios.get('http://127.0.0.1:8000/CRS/questions/').then(response => {
          console.log(response.data);
          this.QuestionList = response.data.slice();
          console.log(this.QuestionList);
          this.get_QITEM();
        }).catch(error => console.log(error));
      }
    },
    get_QITEM() {
      if (this.checkedTypes.length == 1) {
        const type = this.checkedTypes.toString();
        this.filtedList = this.QuestionList.filter(function (item) {
          return item.Qtype == type;
        });
        console.log(this.filtedList.length);
      } else {
        this.filtedList = this.QuestionList;
      }
    }
  }
}
</script>

<style>
.search_bar {
  background-color: #f3f7fc;
}

.normal-btn {
  width: 200px;
}

.result_container {
  padding: 6px;
}
</style>