import './App.css'
import Balanc from './Account/Balanc'
import PersonAcc from './Account/personal-account'

// import Person from './Components/Header/Person'


// import {Main1} from './Pages/main1'
// import {Person} from './Pages/personal-account'
// import {Trails} from './Pages/trails'
// import {Voting} from './Pages/voting'


export default function App() {


  return (
    <>
      <header>Личный кабинет</header>
      <PersonAcc />
      <Balanc/>
    </>

  )
}


