import { Link } from "react-router-dom";
import videobg from "../assets/bgvideo2.mp4";
import "../styles/Home.css";
export default function Hero() {
  return (
    <section className="start-video">
      <div
        className="position-absolute fw-bold text-white"
        style={{
          color: "#fff",
          margin: "1rem",
          fontSize: "20px",
          zIndex: "2",
        }}
      >
        <h2>AutoLex</h2>
      </div>
      <div className="start-video__overlay"></div>
      <video src={videobg} autoPlay loop muted />

      <div className="start-video__content h-100 container-custom position-absolute video-content">
        <div className="d-flex h-100 align-items-center start-video__content-width">
          <div className="text-white">
            <h1 className="start-video__heading fw-bold mb-4">
              Your pathway to effortless learning !
            </h1>
            <p className="lead mb-4">Where Waste Reshapes Our World</p>
            <Link to="/upload" className="mt-2 btn btn-lg btn-outline-light">
              Get started
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}
