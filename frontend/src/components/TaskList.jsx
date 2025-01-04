import { useState } from "react"

function TaskList(){
    const [data,setdata]=useState([])
    return(
        <>
        <table>
            <thead>
                <tr>
                    <th>Task</th>
                    <th>Disp</th>
                </tr>
            </thead>
            <tbody>
                {data.map((value,index)=>(
                    <tr key={index}>
                        <td>{value.tittle}</td>
                        <td>{value.disp}</td>
                    </tr>
                ))}
            </tbody>
        </table>
        </>
    )
}
export default TaskList