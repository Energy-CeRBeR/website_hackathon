export default function Select ({ children, value, onChange }) {
    return (
        <div className="inputbox">
            <select name="gendef" id="gender" className="inputbox" defaultValue={value} onChange={onChange}>
                <option value="Мужской">Мужской</option>
                <option value="Женский">Женский</option>
            </select>
            <span>{children}</span>
        </div>
    )
}