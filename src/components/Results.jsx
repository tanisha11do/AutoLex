import { useEffect, useState } from "react";
import PropTypes from "prop-types";
import "../styles/Results.css";

export default function Results({ result, selectedButton }) {
  const [content, setContent] = useState("");

  useEffect(() => {
    switch (selectedButton) {
      case "transcript":
        setContent(result.transcript || "");
        break;
      case "summary":
        setContent(result.summary || "");
        break;
      case "keywords":
        setContent(result.keywords || "");
        break;
      case "resources":
        setContent(result.resources || "");
        break;
      default:
        setContent("");
        break;
    }
  }, [result, selectedButton]);

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
  }, []);

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
  result: PropTypes.object.isRequired, // Adjust PropTypes according to the structure of your result object
  selectedButton: PropTypes.string.isRequired,
};
