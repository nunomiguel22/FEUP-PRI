import React from 'react';
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import Home from './scenes/home';
import WineDetail from './scenes/wineDetail';


function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/wine/:id" element={<WineDetail />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
