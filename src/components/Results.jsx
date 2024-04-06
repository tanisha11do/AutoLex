import { useEffect } from "react";
import "../styles/Results.css";

export default function Results() {
  useEffect(() => {
    const textarea = document.getElementById("styled-textbox");
    const handleTextareaInput = () => {
      textarea.style.height = "auto";
      textarea.style.height = textarea.scrollHeight + "px";
    };

    textarea.addEventListener("input", handleTextareaInput);

    return () => {
      textarea.removeEventListener("input", handleTextareaInput);
    };
  }, []); // Empty dependency array ensures this effect runs only once after initial render

  return (
    <section className="results" id="results">
      <div className="row">
        <div className="col-md-6 offset-md-3 text-center">
          <h1>Let us study more</h1>
          <p>Here are the results....</p>
          <textarea
            id="styled-textbox"
            className="styled-textbox"
            rows="10"
            cols="20"
            placeholder="Enter your text here..."
          ></textarea>
        </div>
      </div>
    </section>
  );
}
