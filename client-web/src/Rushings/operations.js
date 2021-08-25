import * as api from './api'

export async function getRushingData(sortings = [], filter = '') {
  const data = await api.getRushings(sortings.join(','), filter)
  return data
}
