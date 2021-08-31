import * as api from './api'

export async function getRushingData(sortings = [], filter = '', page = 0, offset = 0) {
  const data = await api.getRushings(sortings.join(','), filter, page, offset)
  return data
}
