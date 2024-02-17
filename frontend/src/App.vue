<template>
  <header><h1>Addition and Subtraction Calculator</h1></header>
  <div>
    <!-- Form for calculator -->
    <form>
      <!-- Input for number 1 -->
      Number 1
      <input
        type="text"
        id="num1"
        placeholder="Enter Number 1"
        v-model="num1" 
      />
      <br />
      <br />

      <!-- Input for number 2 -->
      Number 2
      <input
        type="text"
        id="num2"
        placeholder="Enter Number 2"
        v-model="num2"
      />

      <br />
      <br />

      <!-- Button for addition -->
      <button style="margin: 10px" type="button" id="add" @click="add()">
        Add
      </button>

      <!-- Button for subtraction -->
      <button type="button" id="Subtract" @click="subtract()">Subtract</button>
    </form>
  </div>

  <div>
    <!-- Display of results -->
    <h2>{{ result }}</h2>
  </div>
</template>

<script>


export default {
  name: 'App',
  // Data for the calculator
  data() {
    return {
      num1: 0,
      num2: 0,
      result: null
    }
  },
  components: {

  },
  methods: {
    // Function to call the add API
    async add(){
      // Check if the input is empty (replace with 0 if empty)
      const first_num = this.num1 === "" ? 0 : this.num1;
      const second_num = this.num2 === "" ? 0 : this.num2;

      // Create form data
      const formData = new URLSearchParams();
      formData.append('first_num', first_num);
      formData.append('second_num', second_num);

      // Create requestOptions to pass when calling the API
      var requestOptions = {
        method: 'POST',
        body: formData,
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      };

      try{
        // Call the add API
        const response = await fetch('http://127.0.0.1:5000/add', requestOptions);
        // Get the data that is coming back from the API
        const data = await response.json();
        // Set the result to the data that is coming back from the API
        this.result = "Result: " + data.result;
      } catch (error) {
        // Log the error if there is any
        console.error('Error:', error);
      }
    },

    // Function to call the subtract API
    async subtract(){
      // Check if the input is empty (replace with 0 if empty)
      const first_num = this.num1 === "" ? 0 : this.num1;
      const second_num = this.num2 === "" ? 0 : this.num2;

      // Create form data
      const formData = new URLSearchParams();
      formData.append('first_num', first_num);
      formData.append('second_num', second_num);

      // Create requestOptions to pass when calling the API      
      var requestOptions = {
        method: 'POST',
        body: formData,
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      };

      try{
        // Call the subtract API
        const response = await fetch('http://127.0.0.1:5000/subtract', requestOptions);
        // Get the data that is coming back from the API
        const data = await response.json();
        // Set the result to the data that is coming back from the API
        this.result = "Result: " + data.result;
      } catch (error) {
        // Log the error if there is any
        console.error('Error:', error);
      }
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
