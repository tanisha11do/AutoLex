import "../styles/Audio.css";
import upload from "../assets/upload.png";
import topics from "../assets/check-list.png";
import anim from "../assets/Creativity.mp4";

export default function Audio() {
  return (
    <section className="audio-upload" id="audio">
      <div className="ucontainer">
        <button className="upload">
          Upload audio
          <img className="upload1" alt="Upload" src={upload} />
        </button>
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
        <div className="uimage">
          <video className="ui" src={anim} alt="loading..."></video>
        </div>

        {/*<button className='btn3'><img className='logo' alt='resources' src='https://i.postimg.cc/RZ8T3Rzq/education.png'></img><p>Study Materials</p></button>*/}
      </div>
    </section>
  );
}
