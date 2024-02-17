<template>
  <header><h1>Addition and Subtraction Calculator</h1></header>
  <div>
    <form>
      Number 1
      <input
        type="text"
        id="num1"
        placeholder="Enter Number 1"
        v-model="num1" 
      />
      <br />
      <br />
      Number 2
      <input
        type="text"
        id="num2"
        placeholder="Enter Number 2"
        v-model="num2"
      />

      <br />
      <br />

      <button style="margin: 10px" type="button" id="add" @click="add()">
        Add
      </button>

      <button type="button" id="Subtract" @click="subtract()">Subtract</button>
    </form>
  </div>

  <div>
    <h2>Result: {{ result }}</h2>
  </div>
</template>

<script>


export default {
  name: 'App',
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
    async add(){
      const first_num = this.num1 === "" ? 0 : this.num1;
      const second_num = this.num2 === "" ? 0 : this.num2;

      const formData = new URLSearchParams();
      formData.append('first_num', first_num);
      formData.append('second_num', second_num);

      
      var requestOptions = {
        method: 'POST',
        body: formData,
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      };

      try{
        const response = await fetch('http://127.0.0.1:5000/add', requestOptions);
        const data = await response.json();
        this.result = data.result;
      } catch (error) {
        console.error('Error:', error);
      }
    },

    async subtract(){
      const first_num = this.num1 === "" ? 0 : this.num1;
      const second_num = this.num2 === "" ? 0 : this.num2;

      const formData = new URLSearchParams();
      formData.append('first_num', first_num);
      formData.append('second_num', second_num);

      
      var requestOptions = {
        method: 'POST',
        body: formData,
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      };

      try{
        const response = await fetch('http://127.0.0.1:5000/subtract', requestOptions);
        const data = await response.json();
        this.result = data.result;
      } catch (error) {
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
