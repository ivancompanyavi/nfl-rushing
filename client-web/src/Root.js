import React from 'react'

import Content from './Content'
import Header from './Header'
import styles from './Root.modules.css'
import { ThemeProvider } from './Theme'

export default () => (
  <ThemeProvider value="dark">
    <div className={styles.root}>
      <Header />
      <Content />
    </div>
  </ThemeProvider>
)
