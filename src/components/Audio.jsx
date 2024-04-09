import { useState } from "react";

import "../styles/Audio.css";
import upload from "../assets/upload.png";
import topics from "../assets/check-list.png";
import anim from "../assets/Creativity-pana.png";

export default function Audio() {
  const [fileName, setFileName] = useState("No selected file");
  const [transcript, setTranscript] = useState(""); // State to store transcript

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setFileName(file.name);
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault(); // Prevent page reload
    const formData = new FormData(event.target);
    try {
      const response = await fetch("/upload-audio", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setTranscript(data.transcript); // Update transcript state
    } catch (error) {
      console.error("Error uploading file:", error);
    }
  };
  return (
    <section className="audio-upload" id="audio">
      <div className="ucontainer">
        <div className="btns">
          <div className="btnupload">
            <form
              method="post"
              encType="multipart/form-data"
              className="upload text-center"
              onSubmit={handleFormSubmit}
              onClick={() => document.querySelector(".input-field").click()}
            >
              <input
                type="file"
                name="file"
                className="input-field"
                hidden
                accept=".mp3,.mp4"
                onChange={handleFileChange}
              />
              {
                <>
                  <p>Upload Audio</p>
                  <img className="upload1" alt="Upload" src={upload} />
                </>
              }
              <div id="filename">
                <p>{fileName ? fileName : "Choose File"}</p>
              </div>
              <div className="container text-center">
                <input
                  type="submit"
                  id="submitButton"
                  className="btn btn-primary btn-lg"
                  value="Transcribe"
                />
              </div>
            </form>
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
            <button className="btn4">
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
      {transcript !== "" && (
        <div id="speechTranscriptContainer">
          <h1>Transcript</h1>
          <p id="speechText">{transcript}</p>
        </div>
      )}
    </section>
  );
}
