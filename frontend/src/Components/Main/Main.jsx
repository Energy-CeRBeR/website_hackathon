import './Main.css'

import List from '../List/List'

import {background_information} from '../../data'

export default function Main () {
    return (
        <div className='background_information'>
            <div className='conteiner'>
                {background_information.map((dict) => (<List key={Object.keys(dict)[0]} dict={dict}/>))}
            </div>
        </div>
    )
}