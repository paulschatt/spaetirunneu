import type { Team, TeamCreate, TeamUpdate } from '../types/team'
import { ApiService } from './ApiService'

export const teamService = new ApiService<Team, TeamCreate, TeamUpdate>('teams')