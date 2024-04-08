import { useState } from "react";
import axios from "axios";
import "../styles/Audio.css";
import upload from "../assets/upload.png";
import topics from "../assets/check-list.png";
import anim from "../assets/Creativity-pana.png";
import Results from "./Results";

export default function Audio() {
  const [fileName, setFileName] = useState("No selected file");
  const [result, setResult] = useState({});
  const [selectedButton, setSelectedButton] = useState("");

  const handleUpload = async () => {
    try {
      const formData = new FormData();
      formData.append("audio", document.querySelector(".input-field").files[0]);
      formData.append("selectedButton", selectedButton); // Include selected button in form data
      const response = await axios.post(
        "http://localhost:5000/upload-audio",
        formData
      );
      setResult(response.data.result);
    } catch (error) {
      console.error("Error uploading audio:", error);
      alert("Error uploading audio");
    }
  };

  const handleClick = (button) => {
    setSelectedButton(button);
  };

  return (
    <section className="audio-upload" id="audio">
      <div className="ucontainer">
        <div className="btns">
          <div className="btnupload">
            <form
              className="upload"
              onClick={() => document.querySelector(".input-field").click()}
            >
              <input
                type="file"
                name="audio"
                className="input-field"
                hidden
                accept=".mp3,.mp4"
                onChange={({ target: { files } }) => {
                  files[0] && setFileName(files[0].name);
                }}
              />
              {
                <>
                  <p>Upload Audio</p>
                  <img className="upload1" alt="Upload" src={upload} />
                </>
              }
            </form>
            <div id="filename">
              <p>{fileName ? fileName : "Choose File"}</p>
            </div>
          </div>

          <div className="container text-center">
            <button
              type="button"
              className="btn btn-primary btn-lg"
              onClick={handleUpload}
            >
              Submit
            </button>
          </div>

          <div className="options">
            <button className="btn1" onClick={() => handleClick("transcript")}>
              <img
                className="logo"
                alt="transcript"
                src="https://i.postimg.cc/7Z18HfzC/transcription.png"
              ></img>
              <p>Transcript</p>
            </button>
            <button className="btn2" onClick={() => handleClick("summary")}>
              <img
                className="logo"
                alt="summary"
                src="https://i.postimg.cc/cCmmrGsN/text.png"
              ></img>
              <p>Summary</p>
            </button>
            <button className="btn3" onClick={() => handleClick("keywords")}>
              <img className="logo" alt="topics" src={topics}></img>
              <p>Topics</p>
            </button>
            <button className="btn4" onClick={() => handleClick("resources")}>
              <img
                className="logo"
                alt="resources"
                src="https://i.postimg.cc/cCmmrGsN/text.png"
              ></img>
              <p>Resources</p>
            </button>
          </div>
        </div>

        <div className="uimage">
          <img className="ui" src={anim} alt="loading..." />
        </div>
      </div>
      <Results result={result} selectedButton={selectedButton} />
    </section>
  );
}
