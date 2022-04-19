//packages
import { BrowserRouter, Routes, Route, } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';

//components
import Header from './components/Header'

//views
import Home from "./views/Home";
import Curriculum from './views/Curriculum';
import Progress from './views/Progress';
import Schedule from "./views/Schedule";
import Error from "./views/Error";

const App = () => {
  return (
    <>
      <BrowserRouter>
        <Header/>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="Curriculum" element={<Curriculum />} />
          <Route path="Progress" element={<Progress />} />
          <Route path="Schedule" element={<Schedule />} />
          <Route path="*" element={<Error />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;