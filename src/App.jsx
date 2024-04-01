import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import Home from "./pages/Home";
import Upload from "./pages/Upload";

function App() {
  return (
    <Router>
      {/* <Navbar /> */}
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route exact path="/upload" element={<Upload />} />
      </Routes>
    </Router>
  );
}

export default App;
