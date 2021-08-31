import React from 'react'

import styles from './Pager.modules.css'

export default ({ total, offset, value, onPage }) => {
  const numOfPages = Math.ceil(total / offset)

  let items = []
  for (let i = 0; i < numOfPages; i++) {
    items.push(
      <button
        key={`pager_${i}`}
        className={`${styles.item} ${value === i ? styles.active : ''}`}
        onClick={() => onPage(i)}
      >
        {i + 1}
      </button>
    )
  }

  return <div className={styles.pager}>{items}</div>
}
