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
              <div class="tag pt-4 pb-5" id="tagwrapper" v-bind:key="i" v-for="i in topicArr">
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
      <p class="has-text-centered subtitle is-5" v-if="this.filtedList.length > 0"> Total: {{ this.filtedList.length }}
        questions</p>
      <div v-if="noResult" class="has-text-centered is-size-5 is-dark">
        No Result Found.
      </div>
      <div class="result_box" v-bind:key="idx" v-for="idx, index in filtedList">
        <div class="result_container container">
          <div class="box result_box">
            <!-- tag -->
            <div class="level">
              <div class="level-left">
                <div class="level-item">
                  <span class="tag is-link is-light">{{ idx.Qtype }}</span><br>
                </div>
                <div class="level-item" v-bind:key="i" v-for="i in idx.category">
                  <span class="tag is-primary is-light"> {{ getName(i) }}</span>
                </div>
              </div>
            </div>
            <!-- question string -->
            <span v-if="idx.statement.length > 0">
              {{ index + 1 }}.&nbsp;
              <span v-if="idx.statement.length > 0">{{ idx.statement }}</span>
              <p>{{ idx.string }}</p>
            </span>
            <span v-else>
              {{ index + 1 }}.&nbsp;
              {{ idx.string }}
            </span>

            <figure class="image">
              <img class="p-1" v-bind:src="imgURL" v-if="get_img(idx.image)">
            </figure>

            <div class="JsonColumns" v-if="formatDes(idx.description)">
              <div class="columns is-mobile" v-bind:key="d" v-for="d in descrArray">
                <div class="column jcolumn is-narrow">
                  <p>{{ d.name }}&nbsp;</p>
                </div>
                <div class="column jcolumn">
                  <p>{{ d.data }}&nbsp;</p>
                </div>
              </div>
            </div>
            <!-- MC OPTIONS -->
            <div class="JsonColumns" v-if="getOpt(idx.options) === 'text'">
              <div class="columns is-mobile" v-bind:key="o" v-for="o in optionsArray">
                <div class="column jcolumn is-narrow">
                  <p>{{ o.name }}.&nbsp;</p>
                </div>
                <div class="column jcolumn">
                  <p>{{ o.data }}&nbsp;</p>
                </div>
              </div>
            </div>

            <div class="JsonColumns" v-if="getOpt(idx.options) === 'table'">
              <div v-bind:key="o" v-for="o in optionsArray"></div>
              <table class="table is-narrow">
                <thead>
                  <tr>
                    <th class="noBorder"></th>
                    <th class="noBorder" v-for="opt in tableArray" v-bind:key="opt">{{ opt.name }}</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(option, index) in optionsArray" :key="index">
                    <td class="noBorder">{{ option.name }}</td>
                    <td class="noBorder" v-for="(dataItem, dataIndex) in option.data" :key="dataIndex">
                      {{ dataItem.opt }}
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div class="JsonColumns" v-if="getOpt(idx.options) === 'image'">
              <div class="columns" v-bind:key="o" v-for="o in optionsArray">
                <div class="column jcolumn is-narrow">
                  <p>{{ o.name }}.&nbsp;</p>
                </div>
                <div class="column jcolumn">
                  <figure class="mcImage">
                    <img class="mcImg" v-bind:src="imgURL" v-if="get_img(o.data)">
                  </figure>
                </div>
              </div>
            </div>
            <!-- <p v-if="idx.options.length > 0">{{ idx.options }}</p> -->
          </div>
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
      topicArr: [],
      emptyError: false,
      questionList: [],
      filtedList: [],
      childrenList: [],
      imgURL: '',
      noResult: false,
      descrArray: [],
      optionsArray: [],
      tableArray: [],
      topics: [{ "text": "Algorithm Design", "value": "ALGO" }, { "text": "Basic Machine Organisation", "value": "BMO" }, { "text": "Computer System", "value": "COM" }, { "text": "Data Manipulation and Analysis", "value": "DM" }, { "text": "Data Organisation and Data Control", "value": "DO" }, { "text": "Elementary Web Authoring", "value": "ELEWEB" }, { "text": "Health and Ethical Issues", "value": "HEALTH" }, { "text": "Information Processing", "value": "INFO" }, { "text": "Intellectual Property", "value": "IP" }, { "text": "Internet Services and Applications", "value": "NETSEV" }, { "text": "Multimedia Elements", "value": "MEDIA" }, { "text": "Networking and Internet Basics", "value": "NETBAS" }, { "text": "Program Development", "value": "PROGRAM" }, { "text": "Spreadsheets and Databases", "value": "SD" }, { "text": "Threats and Security on the Internet", "value": "THREAT" }]
    }
  },
  components: {

  },
  methods: {
    setTopic: function (e) {
      this.topicArr.push(e);
      // console.log(this.topicArr);
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
      const idx = this.topicArr.indexOf(val);
      if (idx > -1) {
        this.topicArr.splice(idx, 1);
      }
      //console.log(this.topicArr);
    },
    async search() {
      console.log("checkedTypes: " + this.checkedTypes + " " + this.checkedTypes.length);
      console.log("topicArr: " + this.topicArr + " " + this.topicArr.length);
      if (this.checkedTypes.length == 0 && this.topicArr.length == 0) {
        this.emptyError = true;
      } else {
        // const quest_form = { 'Qtype': this.checkedTypes.toString(), 'category': this.topicArr.toString() };
        axios.get('http://127.0.0.1:8000/CRS/questions/').then(response => {
          console.log(response.data);
          let questions = response.data;
          console.log(questions);
          this.questionList = questions.slice();
          this.get_QITEM();
          if (this.topicArr.length >= 1) this.get_FilteredItems(this.topicArr);
          this.get_Children(this.filtedList);

        }).catch(error => console.log(error));
      }
    },
    get_Children: function (questions) {
      let filteredQuestions = questions.map(q => {
        if (q.parentQID !== null) {
          let parentQuestion = questions.find(parent => parent.QID === q.parentQID);
          if (parentQuestion) {
            // parentQuestion.children = parentQuestion.children || {};
            //console.log("uwu: " + JSON.stringify(q, null, 4));
            //parentQuestion.children[q.QID] = q;
            return null;
          }
        }
        return q;
      }).filter(q => q !== null);
      this.childrenList = filteredQuestions.slice();
      console.log(this.childrenList);
    },
    get_QITEM() {
      if (this.checkedTypes.length == 1) {
        const type = this.checkedTypes.toString();
        this.filtedList = this.questionList.filter(function (item) {
          return item.Qtype == type;
        });
        console.log(this.filtedList.length);
        // console.log(this.filtedList[1].category);
      } else {
        this.filtedList = this.questionList;
      }
      console.log("Final list: " + this.filtedList.length);
    },
    get_FilteredItems(arr) {
      this.filtedList = this.filtedList.filter(function (item) {
        for (var i = 0; i < arr.length; i++) {
          if (item.category.includes(arr[i])) {
            return true;
          }
        }
      })
      this.filtedList == 0 ? this.noResult = true : this.noResult = false;
      console.log("Final list: " + this.filtedList);
    },
    get_img(img) {
      if (img != null) {
        //console.log(img);
        const img_url = "http://127.0.0.1:8000" + img;
        this.imgURL = img_url;
        return true;
      }
      return false;
    },
    formatDes(arr) {
      if (arr.length > 0) {
        const clearStr = JSON.parse(arr);
        this.descrArray = clearStr;
        return true;
      }
      return false;
    },
    getOpt(arr) {
      if (arr.length > 0) {
        const clearStr = JSON.parse(arr);
        this.optionsArray = clearStr[0].options;
        const type = clearStr[0].type;
        switch (type) {
          case 'text':
            return 'text';
          case 'table':
            this.tableArray = this.optionsArray[0].data;
            return 'table';
          case 'image':
            return 'image';
          default:
            return 'text';
        }
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

.mcImage {
  padding: 4px
}

@media screen and (min-width: 1024px) {
  .image img {
    display: block;
    height: 240px;
    width: auto;
  }

  .mcImg {
    display: block;
    height: 150px;
    width: auto;
    padding-right: 10px;
  }
}

@media screen and (max-width: 768px) {
  .image img {
    display: block;
    width: auto;
  }

  .level-item {
    display: inline-block;
  }

}

@media screen and (min-width: 769px) and (max-width: 1023px) {
  .image img {
    display: block;
    width: auto;
  }

}

.jcolumn {

  padding: 5px !important;
}

.JsonColumns {
  padding: 20px;
}

.noBorder {
  border: none !important;
}
</style>