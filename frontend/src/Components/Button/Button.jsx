import { Children } from "react";
import './Button.css'
export default function Button({children, onClick}){
    function handleClick(){

    }
    return(
        <button className="" type="submit">{children}</button>
    )
}