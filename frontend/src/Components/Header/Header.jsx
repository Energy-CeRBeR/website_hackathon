import Button from "../Button/Button"
import './Header.css'
export default function Header(){
    return(
            <section>
                {/* <Button>Главная</Button> */}
                <Button>Личный кабинет</Button>
                <Button>Голосование</Button>
            </section>
    )
}