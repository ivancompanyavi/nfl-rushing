import React, { useState } from 'react'

import styles from './Table.modules.css'

export default ({ data = [], onSort, sortings = [] }) => {
  if (!data || data.length === 0) {
    return null
  }

  const sortItem = (field) => {
    const sortIndex = sortings.findIndex((s) => {
      if (s[0] === '-') {
        return s.substr(1) === field
      }
      return s === field
    })
    if (sortIndex !== -1) {
      if (sortings[sortIndex][0] === '-') {
        sortings.splice(sortIndex, 1)
      } else {
        sortings[sortIndex] = `-${field}`
      }
    } else {
      sortings.push(field)
    }
    onSort(sortings)
  }

  const getArrow = (field) => {
    if (sortings.includes(field)) {
      return <i>&uarr;</i>
    } else if (sortings.includes(`-${field}`)) {
      return <i>&darr;</i>
    }
    return <i>&nbsp;</i>
  }

  const headers = Object.keys(data[0])

  return (
    <table className={styles.table}>
      <thead>
        <tr>
          {headers.map((h, i) => (
            <th key={`table_header_${i}`} onClick={() => sortItem(h)}>
              {getArrow(h)}
              {h.replace(/_/g, ' ')}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((d, i) => (
          <tr key={`table_row_${i}`}>
            {Object.values(d).map((value, j) => (
              <td key={`table_row_${i}_${j}`}>{value}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  )
}
