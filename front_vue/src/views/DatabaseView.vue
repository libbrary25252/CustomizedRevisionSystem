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
            </div>
          </div>
          <article class="message is-small is-danger" v-if="!validMC">
            <div class="message-body">
              This field cannot be empty.
            </div>
          </article>

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
          <article class="message is-small is-danger" v-if="!validStr">
            <div class="message-body">
              This field cannot be empty.
            </div>
          </article>
          <article class="message is-small is-danger" v-if="!validLen">
            <div class="message-body">
              Inputted string is too short, it requires at least 10 characters.
            </div>
          </article>

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
                <div class="columns is-mobile" v-bind:key="o" v-for="o in textOpt[0].options">
                  <div class="column is-narrow">
                    <p>{{ o.name }}.&nbsp;</p>
                  </div>
                  <div class="column">
                    <span><input type="text" v-model="o.data"></span>
                  </div>
                </div>
              </div>
            </div>
            <article class="message is-small is-danger" v-if="!validOpt">
              <div class="message-body">
                All Options fields must be filled.
              </div>
            </article>
          </div>
          <div class="field is-grouped">
            <div class="control">
              <button class="button is-link" @click.prevent="submit">Submit</button>
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
      validMC: true,
      validOpt: true,
      validStr: true,
      validLen: true,
      topics: [{ "text": "Algorithm Design", "value": "ALGO" }, { "text": "Basic Machine Organisation", "value": "BMO" }, { "text": "Computer System", "value": "COM" }, { "text": "Data Manipulation and Analysis", "value": "DM" }, { "text": "Data Organisation and Data Control", "value": "DO" }, { "text": "Elementary Web Authoring", "value": "ELEWEB" }, { "text": "Health and Ethical Issues", "value": "HEALTH" }, { "text": "Information Processing", "value": "INFO" }, { "text": "Intellectual Property", "value": "IP" }, { "text": "Internet Services and Applications", "value": "NETSEV" }, { "text": "Multimedia Elements", "value": "MEDIA" }, { "text": "Networking and Internet Basics", "value": "NETBAS" }, { "text": "Program Development", "value": "PROGRAM" }, { "text": "Spreadsheets and Databases", "value": "SD" }, { "text": "Threats and Security on the Internet", "value": "THREAT" }],
      qtype: '',
      success: false,
      qstate: '',
      qstr: '',
      qid: '',
      topicArr: [],
      topicStr: '',
      imgFormData: '',
      selectedImage: '',
      desOpt: [] = [{ "name": '', "data": '' }],
      DesList: '',
      textOpt: [] = [{ "type": "text", "options": [{ "name": "A", "data": '' }, { "name": "B", "data": '' }, { "name": "C", "data": '' }, { "name": "D", "data": '' }] }],
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
    async uploadImage() {
      // Create a FormData object
      this.selectedImage = this.$refs.fileInput.files[0];
      this.imgFormData = new FormData();
      this.imgFormData.append('image', this.selectedImage);
      // const id = this.qid;
      // // Use axios to make a POST request to your Django backend
      console.log(this.imgFormData)

    },
    clearImage() {
      this.selectedImage = '';
      this.imgFormData = '';
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
      this.topicArr = [];
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
          console.log(this.topicArr.length)
          this.topicStr = this.topicArr.toString();
          // console.log("topic arr: " + str)
          return true;
        }).catch(error => {
          console.log(error);
          return false;
        });
    },
    async submitForm() {
      // console.log(this.desOpt)
      // console.log(this.textOpt)
      // console.log(this.imageName)
      // console.log(this.imgfile)

      // console.log("JSON 1: " + JSON.stringify(this.desOpt))
      // console.log("JSON 2: " + JSON.stringify(this.textOpt))
      // console.log(this.qtype)

      //let topic = this.getresult();
      // const Topicarr = this.topicArr.toString();
      // console.log(Topicarr)
      const Qstring = this.qstate.trim().length > 0 ? this.qstate.trim() + " " + this.qstr.trim() : this.qstr.trim();
      console.log("QQstring: " + Qstring)
      const DesStr = this.setDesc(this.desOpt)
      let Opt = ''
      if (this.qtype == 'MC') {
        Opt = JSON.stringify(this.textOpt)
      } else if (this.qtype == 'LQ') {
        Opt = ''
      }
      const formData = {
        'QID': this.qid,
        'Qtype': this.qtype,
        'statement': this.qstate,
        'string': Qstring,
        'options': Opt,
        'description': DesStr,
        'category': this.topicStr,
        //'category': "DO",
      }
      // const formData = {
      //   QID: this.qid,
      //   statement: '',
      //   string: 'What are the advantages of using the following calendar box over a text box for entering a date?',
      //   Qtype: "MC",
      //   options: "[{\"type\":\"text\",\"options\":[{\"name\":\"A\",\"data\":\"(1) and (2) only\"},{\"name\":\"B\",\"data\":\"(1) and (3) only\"},{\"name\":\"C\",\"data\":\"(2) and (3) only\"},{\"name\":\"D\",\"data\":\"(2) and (3)\"}]}]",
      //   description: "[{\"name\":\"(1)\",\"data\":\"Avoids impossible dates.\"},{\"name\":\"(2)\",\"data\":\"Ensures that the input is error-free.\"},{\"name\":\"(3)\",\"data\":\"Provides a user-friendly interface.\"}]",
      //   category: "DO",
      //   image: 'uploads/images/4333.png'
      // }
      console.log(JSON.stringify(formData))
      await axios.post('/CRS/questions/', formData)
        .then(response => {
          this.success = true;
        }).catch(error => {
          console.log(error);
          return false;
        });
    },
    submit() {
      this.validMC = true;
      this.validOpt = true;
      this.validStr = true;
      this.validLen = true;
      this.genID();

      console.log(this.check())
      if (this.check()) {
        this.getresult().then(response => {
          this.submitForm().then(response => {
            setTimeout(() => {

              if (this.success) {
                axios.post(`/CRS/upload_image/${this.qid}/`, this.imgFormData)
                  .then(response => {
                    // Handle success
                    console.log('Image uploaded successfully');
                    // Do something with the response, such as updating your data or displaying a success message
                  })
                  .catch(error => {
                    // Handle error
                    console.error('Failed to upload image', error);
                    // Display an error message to the user
                  });
              }
            }, 1500)
          });
        });
      }

    },
    close: function (event) {
      this.success = false;
    },
    check() {
      var notValid = false;
      if (this.qtype.length == 0) {
        this.validMC = false;
        notValid = true;
      }
      if (this.qtype == 'MC') {
        for (let index = 0; index < this.textOpt[0].options.length; index++) {
          const element = this.textOpt[0].options[index].data;
          if (element.length < 1) {
            this.validOpt = false;
            notValid = true;
          }
        }
      }
      const tempStr = this.qstr.trim();

      if (tempStr.length == 0) {
        this.validStr = false;
        notValid = true;
      }
      if (tempStr.length < 10 && tempStr.length > 0) {
        this.validLen = false;
        notValid = true;
      }
      if (notValid) {
        return false
      } else return true;
    },
    setDesc(arr) {
      for (let index = 0; index < arr.length; index++) {
        const data = arr[index].data;
        const name = arr[index].name;
        if (data.length < 1 || name.length < 1) {
          return '';
        }
      }
      return JSON.stringify(arr)
    }
  }
}
</script>
  
