<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <page-list style="margin-right: auto; margin-left: auto;"></page-list>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import PageList from "./components/PageList";

export default {
  name: 'app',
  components: {
    HelloWorld,
    PageList
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
