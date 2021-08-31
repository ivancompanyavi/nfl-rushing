import React, { useEffect, useState } from 'react'

import Table from './Table'
import Search from './Search'
import Offsetter from './Offsetter'
import Pager from './Pager'
import { operations } from '../duck'

import styles from './Rushings.modules.css'

const { getRushingData } = operations

export default () => {
  const [data, setData] = useState({ data: [] })
  const [sortings, setSortings] = useState([])
  const [filter, setFilter] = useState('')
  const [page, setPage] = useState(0)
  const [offset, setOffset] = useState(10)

  useEffect(() => {
    async function fetch() {
      const payload = await getRushingData(sortings, filter, page, offset)
      setData(payload)
    }
    fetch()
  }, [])

  const offsetFn = async (v) => {
    setOffset(v)
    await search(sortings, filter, page, v)
  }

  const sortFn = async (v) => {
    setSortings([...v])
    await search(v, filter, page, offset)
  }

  const filterFn = async (v) => {
    await search(sortings, v, page, offset)
  }

  const pageFn = async (v) => {
    setPage(v)
    await search(sortings, filter, v, offset)
  }

  const search = async (s, f, p, o) => {
    const payload = await getRushingData(s, f, p, o)
    setData(payload)
  }

  return (
    <section className={styles.content}>
      <section className={styles.actionBar}>
        <Search value={filter} onChange={(v) => setFilter(v)} onSearch={filterFn} />
        <Offsetter value={offset} onOffset={offsetFn} />
      </section>
      <Table data={data.data} onSort={sortFn} sortings={sortings} />
      <Pager total={data.total} offset={offset} value={page} onPage={pageFn} />
    </section>
  )
}
