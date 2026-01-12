<template>
  <div class="spaetirun">
    <h1>Spätirun</h1>
    <div class="create-form">
      <h2>Schritt 1: Neuen Spätirun Erstellen</h2>
      <input v-model="newSpaetirun.name" placeholder="Name" />
      <button @click="createSpaetirun">Erstellen</button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { spaetirunService } from '../api/spaetirun'
import type { Spaetirun, SpaetirunCreate } from '../types/spaetirun'

export default defineComponent({
  name: 'Spaetirun',
  data() {
      return {
        newSpaetirun: { name: '' } as SpaetirunCreate
      }
    },
  methods: {
    async createSpaetirun() {
      try {
        await spaetirunService.create(this.newSpaetirun)
        this.newSpaetirun = { name: ''}
      } catch (error) {
        console.error('Error creating spaetirun:', error)
      }
    },
  }
})
</script>

<style scoped>
.spaeitrun {
  padding: 20px;
}

.create-form {
  margin-bottom: 30px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.create-form input {
  margin: 5px;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.create-form button {
  margin: 5px;
  padding: 8px 16px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

.items-list {
  margin-top: 20px;
}

.item-card {
  border: 1px solid #ddd;
  padding: 15px;
  margin: 10px 0;
  border-radius: 5px;
  text-align: left;
}

.item-card button {
  margin-top: 10px;
  padding: 5px 10px;
  background-color: #e74c3c;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}
</style>
