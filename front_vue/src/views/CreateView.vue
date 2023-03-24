<template>
  <div class="createQList">
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
              <div class="tag pt-3" id="tagwrapper" v-bind:key="i" v-for="i in TopicArr">
                <span class="tag is-info"> {{ getName(i) }} <button class="delete is-small"
                    @click="removeTopic(i)"></button></span>
              </div>
            </div>
          </div>
        </div>
        <div class="is-fullwidth has-text-centered">
          <button class="button is-link is-rounded block normal-btn" @click="search()">
            <span class="icon">
              <i class="fa fa-search" aria-hidden="true"></i>
            </span>
            <span>Search</span>
          </button>
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
      console.log("checkedTypes: " + this.checkedTypes + " " + this.checkedTypes.length);
      console.log("TopicArr: " + this.TopicArr + " " + this.TopicArr.length);
      axios.get('http://127.0.0.1:8000/CRS/questions/').then(response => {

      }).catch(error => console.log(error));
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
</style>