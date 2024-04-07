import { useState } from "react";
import "../styles/Audio.css";
import upload from "../assets/upload.png";
import topics from "../assets/check-list.png";
import anim from "../assets/Creativity-pana.png";

export default function Audio() {
  
  const [ fileName,setFileName] = useState("No selected file")
  return (
    <section className="audio-upload" id="audio">
      <div className="ucontainer">
        <div className="btns">
          <div className="btnupload">
          <form className="upload" onClick={() => document.querySelector(".input-field").click()}>
          <input type="file" className="input-field" hidden accept=".mp3,.mp4" 
            onChange={({target: {files}}) => {
              files[0] && setFileName(files[0].name)
            }}
          />
            {<><p>Upload Audio</p>
              <img className="upload1" alt="Upload" src={upload} /></>
              }
            
          </form>
          <div id="filename"><p>{fileName ? fileName : 'Choose File'}</p></div>
        </div>
        
        


        <div className="options">
          <button className="btn1">
            <img
              className="logo"
              alt="transcript"
              src="https://i.postimg.cc/7Z18HfzC/transcription.png"
            ></img>
            <p>Transcript</p>
          </button>
          <button className="btn2">
            <img
              className="logo"
              alt="summary"
              src="https://i.postimg.cc/cCmmrGsN/text.png"
            ></img>
            <p>Summary</p>
          </button>
          <button className="btn3">
            <img className="logo" alt="topics" src={topics}></img>
            <p>Topics</p>
          </button>
        </div>
        </div>
        
        <div className="uimage">
          <img className="ui" src={anim} alt="loading..."/>
        </div>

        {/*<button className='btn3'><img className='logo' alt='resources' src='https://i.postimg.cc/RZ8T3Rzq/education.png'></img><p>Study Materials</p></button>*/}
      </div>
    </section>
  );
}
