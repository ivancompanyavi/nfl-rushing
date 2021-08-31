import React from 'react'
import { shallow } from 'enzyme'
import { describe, expect, it } from '@jest/globals'
import Pager from './Pager'

describe('Rushing -> Pager', () => {
  it('should show 2 pages when offset is 10 and there are 11 items', () => {
    component = shallow(<Pager total={11} offset={10} />)
    expect(component.find('button').length).toEqual(2)
  })
  it('should show 4 pages when offset is 10 and there are 40 items', () => {
    component = shallow(<Pager total={40} offset={10} />)
    expect(component.find('button').length).toEqual(4)
  })
  it('should show 1 pages when offset is 10 and there are 1 items', () => {
    component = shallow(<Pager total={1} offset={10} />)
    expect(component.find('button').length).toEqual(1)
  })
})
