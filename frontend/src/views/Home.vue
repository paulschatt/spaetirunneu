<template>
  <div class="container">
    <h1>Start</h1>
    <button @click="goToTeam" class="stacked-button">Team beitreten</button>
    <button @click="goToSpaetirun" class="stacked-button">Spätirun erstellen</button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'Home',
  setup() {
    const router = useRouter()

    const goToSpaetirun = () => {
      router.push('/spaetirun')
    }

    const goToTeam = () => {
          router.push('/team')
    }

    return { goToSpaetirun, goToTeam }
  }
})
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column; /* stack children vertically */
  align-items: center;    /* center horizontally */
  gap: 10px;              /* spacing between buttons */
  margin-top: 50px;
}

.stacked-button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  width: 200px;           /* optional: make buttons same width */
}
</style>