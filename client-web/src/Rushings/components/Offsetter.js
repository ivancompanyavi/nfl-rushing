import React from 'react'

import styles from './Offsetter.modules.css'

export default ({ value, onOffset }) => {
  const values = [5, 10, 20, 30]
  return (
    <div className={styles.offsetter}>
      {values.map((v) => (
        <button
          key={`offsetter_${v}`}
          className={`${styles.item} ${value === v ? styles.active : ''}`}
          onClick={() => onOffset(v)}
        >
          {v}
        </button>
      ))}
    </div>
  )
}
