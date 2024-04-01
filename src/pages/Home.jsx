import "../styles/Home.css";

import Features from "../components/Features";
// import Contact from "../components/Contact";
import Hero from "../components/Hero";
import Aboutus from "../components/Aboutus";

const Home = () => {
  return (
    <div className="container-fluid">
      <Hero />
      <Aboutus />
      <Features />
    </div>
  );
};

export default Home;
