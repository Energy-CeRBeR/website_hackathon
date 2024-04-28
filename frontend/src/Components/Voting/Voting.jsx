import './Voting.css'

import VoitingButton from '../VoitingButton/VoitingButton'

export default function Voting ({ data }) {

    const districts = Object.keys(data)

    function add_voice ({ prop }) {
        console.log(prop.town)
        // put('/${town}_1')
    }

    return (
        <div className='voiting'>
            <h1 className='title'>Голосование</h1>
            {districts.map((district) => (
                <div key={district} className='district'> 
                    <h1>{district} округ</h1> 
                    <ul className='districts'>{Object.keys(data[district]).map((town) => (
                        <li key={town}> {town} | Голоса: {data[district][town]} <VoitingButton onClick={() => put('/' + town + '_1')}/></li>))} 
                    </ul> 
                </div>) )}
        </div>
    )
}