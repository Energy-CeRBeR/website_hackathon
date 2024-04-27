import './List.css'

export default function List (proops) {
    return (
        <>
            <h2>{Object.keys(proops.dict)[0]}</h2>
            <ul>
                {proops.dict[Object.keys(proops.dict)[0]].map((el) => (<li>{el}</li>))}
            </ul>
        </>
    )
}
