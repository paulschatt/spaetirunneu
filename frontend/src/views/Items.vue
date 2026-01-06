<template>
  <div class="items">
    <h1>Items</h1>

    <div class="create-form">
      <h2>Create New Item</h2>
      <input v-model="newItem.name" placeholder="Name" />
      <input v-model="newItem.description" placeholder="Description" />
      <button @click="createItem">Create</button>
    </div>

    <div class="items-list">
      <h2>All Items</h2>
      <div v-for="item in items" :key="item.id" class="item-card">
        <h3>{{ item.name }}</h3>
        <p>{{ item.description }}</p>
        <p>Status: {{ item.is_active ? 'Active' : 'Inactive' }}</p>
        <button @click="deleteItem(item.id)">Delete</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import itemsApi from '../api/items'
import type { Item, ItemCreate } from '../types/item'

export default defineComponent({
  name: 'Items',
  data() {
    return {
      items: [] as Item[],
      newItem: {
        name: '',
        description: ''
      } as ItemCreate
    }
  },
  async mounted() {
    await this.loadItems()
  },
  methods: {
    async loadItems() {
      try {
        this.items = await itemsApi.getItems()
      } catch (error) {
        console.error('Error loading items:', error)
      }
    },
    async createItem() {
      try {
        await itemsApi.createItem(this.newItem)
        this.newItem = { name: '', description: '' }
        await this.loadItems()
      } catch (error) {
        console.error('Error creating item:', error)
      }
    },
    async deleteItem(id: number) {
      try {
        await itemsApi.deleteItem(id)
        await this.loadItems()
      } catch (error) {
        console.error('Error deleting item:', error)
      }
    }
  }
})
</script>

<style scoped>
.items {
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
