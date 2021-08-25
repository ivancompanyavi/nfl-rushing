import React from 'react'

import styles from './Header.modules.css'
import Item from './Item'

export default () => (
  <section className={styles.header}>
    <div className={styles.content}>
      <img className={styles.logo} src="https://www.thescore.com/static/vectors/thescore-logo.svg" />
      <Item title="nfl" />
    </div>
  </section>
)
