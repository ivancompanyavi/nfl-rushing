import React from 'react'
import { useState } from 'react'

import styles from './Theme.modules.css'

const ThemeContext = React.createContext('light')

export const ThemeProvider = ({ value, children }) => {
  const [theme, setTheme] = useState(value)

  let className = {}
  if (theme === 'light') {
    className = styles.light
  } else {
    className = styles.dark
  }

  return (
    <ThemeContext.Provider>
      <div className={className}>{children}</div>
    </ThemeContext.Provider>
  )
}

export const useTheme = () => React.useContext(ThemeContext)
