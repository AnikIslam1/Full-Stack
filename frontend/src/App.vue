<template>
  <div id="app">
    
    <form @submit.prevent="SubmitForm">
      <div class="container">
        <h1>Register</h1>
        <p>Please fill in this form to create an account.</p>
      <hr>

      <label for="User_Name"><b>Name</b></label>
      <input type="text" placeholder="Enter Name" v-model="register.name" required>

      <label for="User_Email"><b>Email</b></label>
      <input type="email" placeholder="Enter Email" v-model="register.mail" required>

      <hr>
      <p>By creating an account you agree to our <a href="#">Terms & Privacy</a>.</p>

      <button type="submit" class="registerbtn">Register</button>
    </div>
  
    <div class="container signin">
      <p>Already have an account? <a href="#">Sign in</a>.</p>
    </div>
  </form>

  </div>
</template>

<script>
// import section
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  data() {
    return{
      register: {
        'name': '',
        'mail': '',
      },
      registers: []
    } 
  },
  async created(){
    await this.getRegister();
  },

  methods: {
    async getRegister(){
      var response = await fetch('http://127.0.0.1:8000/api/register/');
      this.registers = await response.json();
    },
    async SubmitForm(){
      await this.getRegister();
      await fetch('http://127.0.0.1:8000/api/register/',{
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.register)
      });
      await this.getRegister();
    }
  }

}
</script>

<style>
body {
  font-family: Arial, Helvetica, sans-serif;
  background-color: black;
}

* {
  box-sizing: border-box;
}

/* Add padding to containers */
.container {
  padding: 16px;
  background-color: white;
}

/* Full-width input fields */
input[type=text], input[type=email] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus, input[type=email]:focus {
  background-color: #ddd;
  outline: none;
}

/* Overwrite default styles of hr */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* Set a style for the submit button */
.registerbtn {
  background-color: #04AA6D;
  color: white;
  padding: 16px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}

.registerbtn:hover {
  opacity: 1;
}

/* Add a blue text color to links */
a {
  color: dodgerblue;
}

/* Set a grey background color and center the text of the "sign in" section */
.signin {
  background-color: #f1f1f1;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

</style>
