
import Button from '../Components/Button/Button'
import './personal-account.css'

export default function PersonAcc(){
    return(
            <section className="userinfo">
                 <Button>Главная</Button>
                <header>Личный кабинет</header>
            <ul>
                <li><h3>ФИО:</h3></li>
                <li><h3>Номер телефона:</h3></li>
                <li><h3>Место проживания:</h3></li>
            </ul>
            
            </section>
    )
    
}
