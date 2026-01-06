<template>
  <div class="home">
    <h1>Welcome to Spaetirun</h1>
    <p>A FastAPI + Vue.js application with PostgreSQL database</p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'Home'
})
</script>

<style scoped>
.home {
  padding: 20px;
}
</style>
