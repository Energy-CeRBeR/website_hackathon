import './RegistrationForm.css'

import { useState } from "react"

import Input from "../Input"
import Select from "../Select"

export default function RegistrationForm () {
    const [username, setUsername] = useState('')
    const [numberOfPhone, setNumberOfPhone] = useState('')
    const [password, setPassword] = useState('')
    const [repeatPassword, setRepeatPassword] = useState('')
    const [gender, setGender] = useState('')
    const [town, setTown] = useState('')

    return (
        <div className="center">
            <h1>Регистрация</h1>
            <form>
                <Input value={username} onChange={(event) => setUsername(event.target.value)}>ФИО</Input>
                <Input value={numberOfPhone} onChange={(event) => setNumberOfPhone(event.target.value)}>Номер телефона</Input>
                <Input value={password} onChange={(event) => setPassword(event.target.value)}>Пароль</Input>
                <Input value={repeatPassword} onChange={(event) => setRepeatPassword(event.target.value)}>Пароль ещё раз</Input>
                {/* <Select value={gender} onChange={(event) => setGender(event.target.value)}>Пол</Select> */}
                <Input value={town} onChange={(event) => setTown(event.target.value)}>Место проживания</Input>

            </form>
            
        </div>
    )
}
