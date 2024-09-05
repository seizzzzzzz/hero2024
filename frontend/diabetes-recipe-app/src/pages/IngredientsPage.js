// frontend/diabetes-recipe-app/src/pages/IngredientsPage.js

import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

function IngredientsPage() {
  const { state } = useLocation();
  const [ingredients, setIngredients] = useState(state.ingredients || []);
  const [newIngredient, setNewIngredient] = useState('');
  const navigate = useNavigate();

  const handleAddIngredient = () => {
    if (newIngredient && !ingredients.includes(newIngredient)) {
      setIngredients([...ingredients, newIngredient]);
      setNewIngredient('');
    }
  };

  const handleNext = () => {
    navigate('/generate-recipe', { state: { ingredients } });
  };

  return (
    <div>
      <h2>인식된 재료:</h2>
      <ul>
        {ingredients.map((ingredient, index) => (
          <li key={index}>{ingredient}</li>
        ))}
      </ul>
      <input
        type="text"
        value={newIngredient}
        onChange={(e) => setNewIngredient(e.target.value)}
        placeholder="추가할 재료 입력"
      />
      <button onClick={handleAddIngredient}>재료 추가</button>
      <button onClick={handleNext}>다음</button>
    </div>
  );
}

export default IngredientsPage;
