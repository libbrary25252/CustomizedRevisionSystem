<template>
  <div class="parent_box">
    <!-- tag -->
    <div class="level">
      <div class="level-left">
        <div class="level-item">
          <span class="tag is-link is-light">{{ question.Qtype }}</span><br>
        </div>
        <div class="level-item" v-bind:key="i" v-for="i in question.category">
          <span class="tag is-primary is-light"> {{ getName(i) }}</span>
        </div>
      </div>
    </div>
    <!-- question string -->
    <span v-if="question.statement">
      <!-- {{ number + 1 }}.&nbsp; -->
      {{ question.statement }}
      <p>{{ question.string }}</p>
    </span>
    <span v-else>
      <!-- {{ number + 1 }}.&nbsp; -->
      {{ question.string }}
    </span>

    <figure class="image">
      <img class="p-1" v-bind:src="imgURL" v-if="get_img(question.image)">
    </figure>

    <div class="JsonColumns" v-if="formatDes(question.description)">
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
    <div class="JsonColumns" v-if="getOpt(question.options) === 'text'">
      <div class="columns is-mobile" v-bind:key="o" v-for="o in optionsArray">
        <div class="column jcolumn is-narrow">
          <p>{{ o.name }}.&nbsp;</p>
        </div>
        <div class="column jcolumn">
          <p>{{ o.data }}&nbsp;</p>
        </div>
      </div>
    </div>

    <div class="JsonColumns" v-if="getOpt(question.options) === 'table'">
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

    <div class="JsonColumns" v-if="getOpt(question.options) === 'image'">
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
    <!-- <p v-if="question.options.length > 0">{{ question.options }}</p> -->
    <div class="child_box" v-if="question.children && question.children.length > 0">
      <div v-for="child in question.children" :key="child">
        <recursive-component :question="child" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecursiveComponent',
  data() {
    return {
      imgURL: '',
      descrArray: [],
      optionsArray: [],
      tableArray: [],
      topics: [{ "text": "Algorithm Design", "value": "ALGO" }, { "text": "Basic Machine Organisation", "value": "BMO" }, { "text": "Computer System", "value": "COM" }, { "text": "Data Manipulation and Analysis", "value": "DM" }, { "text": "Data Organisation and Data Control", "value": "DO" }, { "text": "Elementary Web Authoring", "value": "ELEWEB" }, { "text": "Health and Ethical Issues", "value": "HEALTH" }, { "text": "Information Processing", "value": "INFO" }, { "text": "Intellectual Property", "value": "IP" }, { "text": "Internet Services and Applications", "value": "NETSEV" }, { "text": "Multimedia Elements", "value": "MEDIA" }, { "text": "Networking and Internet Basics", "value": "NETBAS" }, { "text": "Program Development", "value": "PROGRAM" }, { "text": "Spreadsheets and Databases", "value": "SD" }, { "text": "Threats and Security on the Internet", "value": "THREAT" }],
    }
  },
  props: {
    question: {
      type: Object,
      //default: () => [],
    },
    number: {
      type: Number,
    }
  },
  created() {
    console.log("Created");
    console.log(this.$props.question);
  },
  methods: {
    getName: function (name) {
      for (var i = 0; i < this.topics.length; i++) {
        if (this.topics[i].value == name) {
          return this.topics[i].text;
        }
      }
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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

.parent_box {
  padding-top: 20px;
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
