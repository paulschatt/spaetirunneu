<template>
  <div class="container">
    <h1>Start</h1>
    <button @click="goToTeam" class="stacked-button">Team beitreten</button>
    <button @click="goToSpaetirun" class="stacked-button">Spätirun erstellen</button>
    <v-btn>Klick mich</v-btn>
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
</style>