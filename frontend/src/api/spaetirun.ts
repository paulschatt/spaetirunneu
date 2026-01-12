import type { Spaetirun, SpaetirunCreate, SpaetirunUpdate } from '../types/spaetirun'
import { ApiService } from './apiService'

export const spaetirunService = new ApiService<Spaetirun, SpaetirunCreate, SpaetirunUpdate>('spaetirun');

export default spaetirunService;

spaetirunService.getAll();