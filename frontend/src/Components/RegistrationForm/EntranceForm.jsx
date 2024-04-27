import './RegistrationForm.css'

import { useState } from "react"

import Input from "../Input"

export default function EntranceForm () {
    const [numberOfPhone, setNumberOfPhone] = useState('')
    const [password, setPassword] = useState('')

    return (
        <div className="center">
            <h1>Войти</h1>
            <form>
                <Input value={numberOfPhone} onChange={(event) => setNumberOfPhone(event.target.value)}>Номер телефона</Input>
                <Input value={password} onChange={(event) => setPassword(event.target.value)}>Пароль</Input>
            </form>
            
        </div>
    )
}
