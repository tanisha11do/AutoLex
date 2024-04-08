import { useEffect, useState } from "react";
import PropTypes from "prop-types";
import "../styles/Results.css";

export default function Results({
  transcript,
  summary,
  keywords,
  resources,
  selectedButton,
}) {
  const [content, setContent] = useState("");

  useEffect(() => {
    switch (selectedButton) {
      case "transcript":
        setContent(transcript);
        break;
      case "summary":
        setContent(summary);
        break;
      case "keywords":
        setContent(keywords);
        break;
      case "resources":
        setContent(resources);
        break;
      default:
        setContent("");
        break;
    }
  }, [transcript, summary, keywords, resources, selectedButton]);

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
            value={content}
            readOnly
          ></textarea>
        </div>
      </div>
    </section>
  );
}

Results.propTypes = {
  transcript: PropTypes.string.isRequired,
  summary: PropTypes.string.isRequired,
  keywords: PropTypes.string.isRequired,
  resources: PropTypes.string.isRequired,
  selectedButton: PropTypes.string.isRequired,
};
