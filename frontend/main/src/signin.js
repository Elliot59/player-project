import React from 'react';
import axios from "axios";
import { useState } from "react";



const Signin = () => {

const [name, setName] = useState('None')
const [password, setPassword] = useState('None')

const NameHandle = (event) => {
    event.preventDefault()
    setName(event.target.value)

}

const PasswordHandle = (event) => {
    event.preventDefault()
    setPassword(event.target.value)
}

const Clicked  = async() => {
        let data = {
            "name": name,
            "password": password
        }
        
    await axios.post('http://127.0.0.1:8000/login/', data,{   headers: {
            "Authorization": "Token 26db08d20cdab541be5884daa43e349d7683ca42",
            "content-type": "application/json"
        }}
      )
    .then(res => console.log(res)).catch(err => console.log(err))
    console.log(data)

}




return(
    <div className='form'>
        <label>Username</label>
        <br></br>
        <input name='username' onChange={NameHandle} placeholder='Username'/>
        <br></br>
        <label>Password</label>
        <br></br>
        <input name='password' onChange={PasswordHandle}placeholder='Password'/>
        <br></br>
        <br></br>
        <button type="button" onClick={Clicked} className="btn btn-primary">Submit</button>
    </div>
)
}

export default Signin