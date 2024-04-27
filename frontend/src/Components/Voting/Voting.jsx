import './Voting.css'

import VoitingButton from '../VoitingButton/VoitingButton'

export default function Voting ({ data }) {

    const districts = Object.keys(data)
    console.log(districts)

    return (
        <div className='voiting'>
            <h1 className='title'>Голосование</h1>
            {districts.map((district) => (
                <div className='district'> 
                    <h1>{district} округ</h1> 
                    <ul className='districts'>{Object.keys(data[district]).map((town) => (
                        <li> {town} | Голоса: {data[district][town]} <VoitingButton/></li>))} 
                    </ul> 
                </div>) )}
        </div>
    )
}