import RegistrationForm from "./Components/RegistrationForm/RegistrationForm"
import EntranceForm from "./Components/RegistrationForm/EntranceForm"
import Voting from "./Components/Voting/Voting"
import axios from "axios";
import {useState, useEffect} from 'react'

import { voiting_data } from "./data"

function App() {
  const [districts, setDistricts] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/ratings/').then(r => {
      setDistricts(r.data);
    });
  }, []);

  return (
    <>
      <Voting data={districts} />
    </>
  )}

export default App
