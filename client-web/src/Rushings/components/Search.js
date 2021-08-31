import React from 'react'

import styles from './Search.modules.css'

export default ({ value, onChange, onSearch }) => (
  <div className={styles.search}>
    <input type="text" value={value} onChange={(e) => onChange(e.target.value)} />
    <button onClick={() => onSearch(value)}>Search</button>
  </div>
)
