// frontend/diabetes-recipe-app/src/pages/RecipeDisplayPage.js

import React from 'react';
import { useLocation } from 'react-router-dom';

function RecipeDisplayPage() {
  const { state } = useLocation();
  const recipes = state?.recipes || [];

  return (
    <div>
      <h2>생성된 레시피:</h2>
      {recipes.length > 0 ? (
        <ul>
          {recipes.map((recipe, index) => (
            <li key={index}>
              {recipe.name} - 칼로리: {recipe.calories}, 나트륨: {recipe.sodium}, 탄수화물: {recipe.carbohydrates}
            </li>
          ))}
        </ul>
      ) : (
        <p>해당 재료로 생성된 레시피가 없습니다.</p>
      )}
    </div>
  );
}

export default RecipeDisplayPage;
