import React from 'react';
import '../styles/Upload.css';

function Upload() {
  return (
    <div className="App">
      <header></header>
      <button className='upload'><p>Upload audio</p><img className='upload1' alt='Upload' src='https://i.postimg.cc/j5RWF04m/upload.png'/></button>
      <div className='options'>
        <button className='btn1'><img className='logo' alt='transcript' src='https://i.postimg.cc/7Z18HfzC/transcription.png'></img><p>Transcript</p></button>
        <button className='btn2'><img className='logo' alt='summary' src='https://i.postimg.cc/cCmmrGsN/text.png'></img><p>Summary</p></button>
        <button className='btn3'><img className='logo' alt='topics' src='https://i.postimg.cc/qRcc5H6C/check-list.png'></img><p>Topics</p></button>
        {/*<button className='btn3'><img className='logo' alt='resources' src='https://i.postimg.cc/RZ8T3Rzq/education.png'></img><p>Study Materials</p></button>*/}
      </div>
    </div>
  )
}

export default Upload