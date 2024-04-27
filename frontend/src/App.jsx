import RegistrationForm from "./Components/RegistrationForm/RegistrationForm"
import EntranceForm from "./Components/RegistrationForm/EntranceForm"
import Voting from "./Components/Voting/Voting"

import { voiting_data } from "./data"

function App() {
  const districts = fetch('http://127.0.0.1:8000/ratings/')
  console.log(districts)

  return (
    <>
      <Voting data={voiting_data}/>
    </>
  )
}

export default App
