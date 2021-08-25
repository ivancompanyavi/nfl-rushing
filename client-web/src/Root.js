import React from 'react'

import './normalize.modules.css'

import Content from './Rushings'
import Header from './Header'
import styles from './Root.modules.css'
import { ThemeProvider } from './common/Theme'

export default () => (
  <ThemeProvider value="dark">
    <div className={styles.root}>
      <Header />
      <Content />
    </div>
  </ThemeProvider>
)
