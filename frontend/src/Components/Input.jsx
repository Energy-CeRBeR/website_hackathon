export default function Input ({children,  value, onChange }) {
    return (
        <>
            <div className="inputbox">
                <input value={value} onChange={onChange}/>
                <span>{children}</span>
            </div>
        </>
    )
}
