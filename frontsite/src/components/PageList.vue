<template>
   <div class="grid-content">
      <json-viewer :value="pageList" :expand-depth="5" boxed copyable sort></json-viewer>
   </div>
</template>

<script>
   import { getPagesList } from "../api/pages";
   import JsonViewer from 'vue-json-viewer'

   export default {
      name: "PageList",
      components: { JsonViewer },
      data(){
         return {
            pageList: []
         }
      },
      created() {
         getPagesList().then(
                 res=>{
                    this.pageList=res.data.items
                 }
         )
      }
   }
</script>

<style scoped>
    .grid-content {
       min-height: 36px;
       border-radius: 4px;
       margin: 40px 0 0 50px;
       text-align: left;
       max-width: 500px;
    }


</style>