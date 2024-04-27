import RegistrationForm from "./Components/RegistrationForm/RegistrationForm"
import EntranceForm from "./Components/RegistrationForm/EntranceForm"
import Voting from "./Components/Voting/Voting"

import { voiting_data } from "./data"

function App() {
  return (
    <>
      <Voting data={voiting_data}/>
    </>
  )
}

export default App
