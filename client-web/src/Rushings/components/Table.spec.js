import React from 'react'
import { shallow } from 'enzyme'
import { describe, expect, it } from '@jest/globals'
import Table from './Table'

describe('Rushing -> Table', () => {
  let component
  it('should not render anything if no data provided', () => {
    component = shallow(<Table />)
    expect(component.type()).toBeNull()
  })

  it('should show as many headers as item properties', () => {
    const data = [{ foo: 'foo', bar: 'bar' }]
    component = shallow(<Table data={data} />)
    expect(component.find('th').length).toEqual(2)
  })

  it('should render as many content rows as items', () => {
    const data = [
      { foo: 'foo', bar: 'bar' },
      { foo: 'foo', bar: 'bar' },
      { foo: 'foo', bar: 'bar' },
    ]
    component = shallow(<Table data={data} />)
    expect(component.find('tbody tr').length).toEqual(3)
  })
})
