import React from 'react';
import axios from "axios";
import { useState } from "react";
import querystring from "querystring";


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
    querystring = require('querystring')
    let data = querystring.stringify({
        "username": name,
        "password": password
    })
 
    
    await axios.post({
    method: 'post',
    url: 'http://127.0.0.1:8000/login/',
    data: data,
    headers: {'Content-Type': 'multipart/form-data'}})
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