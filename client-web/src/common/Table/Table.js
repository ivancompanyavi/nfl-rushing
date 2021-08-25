import React, { useState } from 'react'

import './Table.modules.css'

export default ({ data = [], onSort, sortings }) => {
  if (!data || data.length === 0) {
    return null
  }

  const sortItem = (field) => {
    const sortIndex = sortings.findIndex((s) => s === field)
    if (sortIndex !== -1) {
      if (sortings[sortIndex][0] === '-') {
        sortings[sortIndex] = field
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
    <table>
      <thead>
        <tr>
          {headers.map((h) => (
            <th onClick={() => sortItem(h)}>
              {getArrow(h)}
              {h}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((d) => (
          <tr>
            {Object.values(d).map((value) => (
              <td>{value}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  )
}
