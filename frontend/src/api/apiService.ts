import axios, { AxiosInstance } from 'axios'

export class ApiService<T, CreateT = T, UpdateT = T> {
  private api: AxiosInstance
  private resource: string

  constructor(resource: string, baseURL = 'http://localhost:8000/api') {
    this.resource = resource
    this.api = axios.create({ baseURL })
  }

  async getAll(): Promise<T[]> {
    const response = await this.api.get<T[]>(`/${this.resource}`)
    return response.data
  }

  async getById(id: number): Promise<T> {
    const response = await this.api.get<T>(`/${this.resource}/${id}`)
    return response.data
  }

  async create(item: CreateT): Promise<T> {
    const response = await this.api.post<T>(`/${this.resource}`, item)
    return response.data
  }

  async update(id: number, item: UpdateT): Promise<T> {
    const response = await this.api.put<T>(`/${this.resource}/${id}`, item)
    return response.data
  }

  async delete(id: number): Promise<void> {
    await this.api.delete(`/${this.resource}/${id}`)
  }
}