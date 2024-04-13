import { useState } from "react";
import axios from "axios";
import "../styles/Audio.css";
import upload from "../assets/upload.png";
import topics from "../assets/check-list.png";
import anim from "../assets/Creativity-pana.png";

export default function Audio() {
  const [fileName, setFileName] = useState("No selected file");
  const [result, setResult] = useState(null);
  const [activeSection, setActiveSection] = useState(null);

  const handleFileChange = (event) => {
    if (event.target.files && event.target.files.length > 0) {
      const file = event.target.files[0];
      setFileName(file.name);
    } else {
      setFileName("No selected file");
    }
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData();
    formData.append("file", event.target.file.files[0]); // Get the file from the form

    try {
      const response = await axios.post(
        "http://localhost:5000/get-transcript",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      const data = response.data;
      setResult(data);

      // Show success message
      alert("Audio uploaded successfully");
    } catch (error) {
      console.error("Error uploading file:", error);
      // Show error message
      alert("Error uploading file. Please try again.");
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
          <div id="filename">
            <p>{fileName ? fileName : "Choose File"}</p>
          </div>

          <div className="options">
            <button
              className="btn1"
              onClick={() => setActiveSection("transcript")}
            >
              <img
                className="logo"
                alt="transcript"
                src="https://i.postimg.cc/7Z18HfzC/transcription.png"
              ></img>
              <p>Transcript</p>
            </button>
            <button
              className="btn2"
              onClick={() => setActiveSection("summary")}
            >
              <img
                className="logo"
                alt="summary"
                src="https://i.postimg.cc/cCmmrGsN/text.png"
              ></img>
              <p>Summary</p>
            </button>
            <button className="btn3" onClick={() => setActiveSection("topics")}>
              <img className="logo" alt="topics" src={topics}></img>
              <p>Topics</p>
            </button>
            <button
              className="btn4"
              onClick={() => setActiveSection("resources")}
            >
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
      {result && (
        <div id="resultContainer" className="result-container">
          <h1>Result</h1>
          {activeSection === "transcript" && (
            <div>
              <h2>Transcript</h2>
              <p>{result.transcript}</p>
            </div>
          )}
          {activeSection === "summary" && (
            <div>
              <h2>Summary</h2>
              <p>{result.summary}</p>
            </div>
          )}
          {activeSection === "topics" && (
            <div>
              <h2>Keywords</h2>
              <p>{result.keywords.join(", ")}</p>
              <h2>Clusters</h2>
              <ul>
                {result.clusters.map((cluster, index) => (
                  <li key={index}>{cluster}</li>
                ))}
              </ul>
            </div>
          )}
          {activeSection === "resources" && (
            <div>
              <h2>Search Results</h2>
              <ul>
                {result.resources.map((resource, index) => (
                  <li key={index}>
                    <a
                      href={resource.Link}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      {resource.Title}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </section>
  );
}
