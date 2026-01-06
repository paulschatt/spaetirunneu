import axios from 'axios'
import type { Item, ItemCreate, ItemUpdate } from '../types/item'

const API_URL = 'http://localhost:8000/api/items'

export default {
  async getItems(): Promise<Item[]> {
    const response = await axios.get<Item[]>(API_URL)
    return response.data
  },

  async getItem(id: number): Promise<Item> {
    const response = await axios.get<Item>(`${API_URL}/${id}`)
    return response.data
  },

  async createItem(item: ItemCreate): Promise<Item> {
    const response = await axios.post<Item>(API_URL, item)
    return response.data
  },

  async updateItem(id: number, item: ItemUpdate): Promise<Item> {
    const response = await axios.put<Item>(`${API_URL}/${id}`, item)
    return response.data
  },

  async deleteItem(id: number): Promise<void> {
    await axios.delete(`${API_URL}/${id}`)
  }
}
