import type { Team, TeamCreate, TeamUpdate } from '../types/spaetirun'
import { ApiService } from './ApiService'

export const spaetirunService = new ApiService<Spaetirun, SpaetirunCreate, SpaetirunUpdate>('spaetirun');

export default spaetirunService;