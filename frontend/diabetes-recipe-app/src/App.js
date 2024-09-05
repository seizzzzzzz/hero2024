// frontend/diabetes-recipe-app/src/App.js

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import UploadPage from './pages/UploadPage';
import IngredientsPage from './pages/IngredientsPage';
import ErrorPage from './pages/ErrorPage';
import RecipeGeneratePage from './pages/RecipeGeneratePage';
import RecipeDisplayPage from './pages/RecipeDisplayPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<UploadPage />} />
        <Route path="/ingredients" element={<IngredientsPage />} />
        <Route path="/error" element={<ErrorPage />} />
        <Route path="/generate-recipe" element={<RecipeGeneratePage />} />
        <Route path="/recipes" element={<RecipeDisplayPage />} />
      </Routes>
    </Router>
  );
}

export default App;
