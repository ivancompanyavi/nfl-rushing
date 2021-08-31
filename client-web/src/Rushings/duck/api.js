const API_URL = 'http://localhost:8000'

export async function getRushings(sortings, filter, page, offset) {
  const response = await fetch(
    `${API_URL}/rushings?sort_by=${sortings}&filter_by=${filter}&page=${page}&offset=${offset}`
  )
  if (!response.ok) {
    throw new Error('Error retrieving the rushing data')
  }
  return response.json()
}
