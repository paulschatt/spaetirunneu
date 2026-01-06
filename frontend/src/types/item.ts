export interface Item {
  id: number
  name: string
  description: string | null
  is_active: boolean
  created_at: string
  updated_at: string | null
}

export interface ItemCreate {
  name: string
  description?: string | null
  is_active?: boolean
}

export interface ItemUpdate {
  name?: string
  description?: string | null
  is_active?: boolean
}
