import React, { useState } from 'react';
import axios from 'axios';

function Create() {
  const [task, setTask] = useState('');
  const handleAdd = () => {
    axios.post('http://localhost:3001/add', { task: task })
      .then(() => location.reload())  // Removed result
      .catch(err => console.log(err));
  }
  return (
    <div className='create_form'>
      <input type="text" placeholder='Enter Task' onChange={(e) => setTask(e.target.value)} />
      <button type="button" onClick={handleAdd}>Create</button>
    </div>
  )
}

export default Create;
