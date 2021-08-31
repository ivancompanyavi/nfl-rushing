import React from 'react'
import { shallow } from 'enzyme'
import { expect, describe, it } from '@jest/globals'

import Offsetter from './Offsetter'

describe('Rushing -> Offsetter', () => {
  let component
  it('should render 4 elements', () => {
    component = shallow(<Offsetter />)
    expect(component.find('button').length).toEqual(4)
  })

  it('should mark as active the "5" value', () => {
    component = shallow(<Offsetter value={5} />)
    expect(component.find('button').at(0).prop('className')).toEqual('item active')
  })

  it('should call "onOffset" when clicking on an item', () => {
    const onOffsetMock = jest.fn()
    component = shallow(<Offsetter onOffset={onOffsetMock} />)
    component.find('button').at(0).simulate('click')
    expect(onOffsetMock).toHaveBeenCalledWith(5)
  })
})
