import React from 'react'

import styles from './Header.modules.css'
import Item from './Item'

const APP_LOGO = 'https://www.thescore.com/static/vectors/thescore-logo.svg'

export default () => (
  <section className={styles.header}>
    <div className={styles.content}>
      <img className={styles.logo} src={APP_LOGO} />
      <Item title="nfl" />
    </div>
  </section>
)
