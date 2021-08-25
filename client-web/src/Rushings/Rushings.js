import React, { useEffect, useState } from 'react'
import Table from '../common/Table/Table'
import { getRushingData } from './operations'

import styles from './Rushings.modules.css'

export default () => {
  const [data, setData] = useState()
  const [sortings, setSortings] = useState([])
  const [filter, setFilter] = useState('')

  useEffect(() => {
    async function fetch() {
      const payload = await getRushingData()
      setData(payload)
    }
    fetch()
  }, [])

  const sort = async (newSortings) => {
    setSortings([...newSortings])
    search()
  }

  const search = async () => {
    const payload = await getRushingData(sortings, filter)
    setData(payload)
  }

  return (
    <section className={styles.content}>
      <section>
        <input type="text" value={filter} onChange={(e) => setFilter(e.target.value)} />
        <button onClick={search}>Search</button>
      </section>
      <Table data={data} onSort={sort} sortings={sortings} />
    </section>
  )
}
