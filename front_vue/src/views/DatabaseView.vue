<template>
  <div class="section">
    <article v-if="getRole()" class="message is-danger">
      <div class="message-header">
        <p>Warning</p>
      </div>
      <div class="message-body">
        You are not authenticated to access this function. Only <strong>teacher or admin</strong> can modify the database.
      </div>
    </article>
    <div v-else>
      <div class="notification is-primary is-light" v-if="success">
        <button class="delete" @click="close" ref="closeBtn"></button>
        Successfully saved!
      </div>
      <p class="title is-size-4-mobile mt-1">
        Add your questions to database
      </p>
      <p class=" is-size-5-mobile subtitle">
        Model will process your uncatergorised questions into database
      </p>
      <div class="container is-fluid">
        <form class="notification is-light" @submit.prevent="submitQuestion">
          <div class="field">
            <label class="label">Question Type</label>
            <div class="control">
              <label class="radio">
                <input type="radio" v-model="qtype" name="question" value="LQ">
                Long Question
              </label>
              <label class="radio">
                <input type="radio" v-model="qtype" name="question" value="MC">
                Multiple Choice Question
              </label>
              <p class="help is-danger" v-if="Notvalid()">This field cannot be empty</p>
            </div>
          </div>

          <div class="field">
            <label class="label">Statement</label>
            <div class="control">
              <textarea class="input" type="text" placeholder="Text input" v-model="qstate"></textarea>
            </div>
          </div>

          <div class="field">
            <label class="label">Question String</label>
            <div class="control">
              <textarea class="input" type="text" placeholder="Text input" v-model="qstr"></textarea>
            </div>
          </div>

          <div class="field">
            <label class="label" for="image">Image</label>
            <input type="file" id="imageUpload" name="image" @change="uploadImage" ref="fileInput" accept="image/*">
            <button class="button is-small" @click.prevent="clearImage">Clear Image</button>
          </div>


          <div class="field" v-if="qtype == 'MC'">
            <div class="field">
              <label class="label">Description <button class="button is-dark is-small is-rounded"
                  @click="addDes">Add</button></label>

              <div class="control">
                <div class="columns is-mobile" v-bind:key="o" v-for="o in desOpt">
                  <div class="column is-narrow">
                    <input type="text" v-model="o.name">
                  </div>
                  <div class="column is-narrow">
                    <span><input type="text" v-model="o.data"> <button class="delete is-small"
                        @click="removeDes(o)"></button></span>
                  </div>
                </div>
              </div>
            </div>

            <div class="field">
              <label class="label">Options</label>
              <div class="control">
                <div class="columns is-mobile" v-bind:key="o" v-for="o in textOpt">
                  <div class="column is-narrow">
                    <p>{{ o.name }}.&nbsp;</p>
                  </div>
                  <div class="column">
                    <span><input type="text" v-model="o.data"></span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="field is-grouped">
            <div class="control">
              <button class="button is-link" @click.prevent="submitForm">Submit</button>
            </div>
            <div class="control">
              <button class="button is-link is-light" @click="reset">Cancel</button>
            </div>
          </div>
        </form>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'DatabaseView',
  data() {
    return {
      topics: [{ "text": "Algorithm Design", "value": "ALGO" }, { "text": "Basic Machine Organisation", "value": "BMO" }, { "text": "Computer System", "value": "COM" }, { "text": "Data Manipulation and Analysis", "value": "DM" }, { "text": "Data Organisation and Data Control", "value": "DO" }, { "text": "Elementary Web Authoring", "value": "ELEWEB" }, { "text": "Health and Ethical Issues", "value": "HEALTH" }, { "text": "Information Processing", "value": "INFO" }, { "text": "Intellectual Property", "value": "IP" }, { "text": "Internet Services and Applications", "value": "NETSEV" }, { "text": "Multimedia Elements", "value": "MEDIA" }, { "text": "Networking and Internet Basics", "value": "NETBAS" }, { "text": "Program Development", "value": "PROGRAM" }, { "text": "Spreadsheets and Databases", "value": "SD" }, { "text": "Threats and Security on the Internet", "value": "THREAT" }],
      qtype: '',
      success: false,
      uploadedImage: null,
      imageName: '',
      qstate: '',
      qstr: '',
      qid: '',
      topicArr: [],
      imgFormData: '',
      imgfile: null,
      desOpt: [] = [{ "name": '', "data": '' }],
      DesList: '',
      textOpt: [] = [{ "name": "A", "data": '' }, { "name": "B", "data": '' }, { "name": "C", "data": '' }, { "name": "D", "data": '' }],
    }
  },
  mounted() {
    this.genID();
  },
  methods: {
    getRole() {
      const role = localStorage.getItem('role');
      if (role == 1) {
        return false;
      }
      return true;
    },
    Notvalid() {
      return false;
    },
    genID() {
      const id = Math.floor(Math.random() * 9000) + 1000;
      console.log("id: " + id)
      this.qid = id;
    },
    uploadImage(event) {
      this.imgfile = event.target.files[0];
      this.imageName = 'uploads/images/' + this.qid.toString() + '.png'; // replace with your desired file name
      // const formData = new FormData();
      // formData.append('image', file, this.imageName);
    },
    clearImage() {
      this.uploadedImage = null;
      this.imageName = '';
      this.$refs.fileInput.value = null; // clear the file input
    },
    reset() {
      window.location.reload();
    },
    addDes() {
      this.desOpt.push({ "name": '', "data": '' })
    },
    removeDes(val) {
      const idx = this.desOpt.indexOf(val);
      if (idx > -1) {
        this.desOpt.splice(idx, 1);
      }
    },
    getValue(name) {
      for (var i = 0; i < this.topics.length; i++) {
        if (this.topics[i].text == name) {
          return this.topics[i].value;
        }
      }
    },
    async getresult() {
      console.log(this.qstr)
      await axios.post('/modelapi/api', { 'text': this.qstr })
        .then(response => {
          console.log(response.data);
          const topics = response.data["prediction"]
          if (topics.length >= 1) {
            for (var i = 0; i < topics.length; i++) {
              const val = this.getValue(topics)
              this.topicArr.push(val)
            }
          }
          // question.result = topics || "No result";
          console.log(this.topicArr)
          return true;
        }).catch(error => {
          console.log(error);
          return false;
        });
    },
    async submitForm() {
      console.log(this.desOpt)
      console.log(this.textOpt)
      console.log(this.imageName)
      console.log(this.imgfile)

      const dData = {
        type: "text",
        options: [(this.textOpt)]
      }
      if (this.getresult()) {
        // const formData = new FormData();
        // formData.append('QID', this.qid);
        // formData.append('statement', this.qstate);
        // formData.append('string', this.qstr);
        // formData.append('Qtype', this.qtype);
        // formData.append('options', JSON.stringify(this.desOpt));
        // formData.append('description', dData);
        // formData.append('category', this.topicArr);
        // formData.append('image', this.imgfile, this.imageName); // add the image file to the FormData object
        // console.log(formData)
        const formData = {
          QID: '3123',
          statement: '',
          string: 'What are the advantages of using the following calendar box over a text box for entering a date?',
          Qtype: "MC",
          options: "[{\"type\":\"text\",\"options\":[{\"name\":\"A\",\"data\":\"(1) and (2) only\"},{\"name\":\"B\",\"data\":\"(1) and (3) only\"},{\"name\":\"C\",\"data\":\"(2) and (3) only\"},{\"name\":\"D\",\"data\":\"(2) and (3)\"}]}]",
          description: "[{\"name\":\"(1)\",\"data\":\"Avoids impossible dates.\"},{\"name\":\"(2)\",\"data\":\"Ensures that the input is error-free.\"},{\"name\":\"(3)\",\"data\":\"Provides a user-friendly interface.\"}]",
          category: "DO",
          image: 'uploads/images/4333.png'
        }
        console.log(JSON.stringify(formData))
        await axios.post('/CRS/questions/', formData)
          .then(response => {
            this.success = true;
          }).catch(error => {
            console.log(error);
            return false;
          });

      }
    },
    close: function (event) {
      this.success = false;
    },

  }
}
</script>
  
