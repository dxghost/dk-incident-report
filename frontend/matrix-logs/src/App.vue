<template>
  <div id="app">
    <h1>Logs</h1>
    <div v-for="post in posts" v-bind:key="post.id">
      <p> {{ post.message }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Matrix",
  data() {
    return {
      posts: [],
    };
  },
  methods: {
    async getData() {
      try {
        const response = await this.$http.get("http://localhost:8000/reports/");
        // JSON responses are automatically parsed.
        this.posts = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.getData();
  },
};
</script>

<style>
@font-face {
  font-family: "Spotnik";
  src: local("Spotnik"), url(./fonts/Spotnikdemo-K7dpy.ttf) format("truetype");
}
#app {
  font-family: monospace;
  font-size: 2vh;
  color: #19ff71;
}
html {
  padding: 0;
  margin: 0;
  width: 100%;
  background-color: black;
}
h1{
  font-size:7vh;
  font-family:Spotnik;
  color: gold;
  text-align: center;
  margin:0;
  padding:0;
}
p{
 margin: 0;
 padding: 0;
}
</style>
