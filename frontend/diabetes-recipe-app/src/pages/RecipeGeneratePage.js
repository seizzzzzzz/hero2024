// frontend/diabetes-recipe-app/src/pages/RecipeGeneratePage.js

import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

function RecipeGeneratePage() {
  const { state } = useLocation();
  const [bmr, setBmr] = useState('');
  const [bloodSugar, setBloodSugar] = useState('');
  const navigate = useNavigate();
  const ingredients = state?.ingredients || [];

  const handleRecipeGeneration = async () => {
    const params = new URLSearchParams({
      ingredients: ingredients.join(','),
      bmr,
      blood_sugar: bloodSugar,
    });

    try {
      const response = await fetch(`/api/filter_recipes/?${params}`);
      const data = await response.json();
      navigate('/recipes', { state: { recipes: data.recipes } });
    } catch (err) {
      navigate('/error', { state: { message: "레시피 생성 중 오류가 발생했습니다." } });
    }
  };

  return (
    <div>
      <h2>재료에 따른 레시피 생성:</h2>
      <ul>
        {ingredients.map((ingredient, index) => (
          <li key={index}>{ingredient}</li>
        ))}
      </ul>
      <input 
        type="text" 
        value={bmr} 
        onChange={(e) => setBmr(e.target.value)} 
        placeholder="BMR 입력"
      />
      <input 
        type="text" 
        value={bloodSugar} 
        onChange={(e) => setBloodSugar(e.target.value)} 
        placeholder="혈당 수치 입력"
      />
      <button onClick={handleRecipeGeneration}>레시피 생성</button>
    </div>
  );
}

export default RecipeGeneratePage;
