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

export async function fetchCSV(sortings, filter) {
  const response = await fetch(`${API_URL}/rushings/download?sort_by=${sortings}&filter_by=${filter}`)
  const text = await response.text()
  saveAsFile(text, 'rushings.csv')
  if (!response.ok) {
    throw new Error('Error downlaoding rushing data')
  }
}

function saveAsFile(text, filename) {
  const type = 'text/csv'
  const blob = new Blob([text], { type })

  const a = document.createElement('a')
  a.href = URL.createObjectURL(blob)
  a.download = filename
  a.click()
}
