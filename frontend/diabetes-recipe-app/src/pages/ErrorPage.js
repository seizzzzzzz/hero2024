// frontend/diabetes-recipe-app/src/pages/ErrorPage.js

import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

function ErrorPage() {
  const navigate = useNavigate();
  const { state } = useLocation();
  const message = state?.message || "오류가 발생했습니다.";

  const handleRetry = () => {
    navigate('/');
  };

  const handleManualCorrection = () => {
    navigate('/ingredients', { state: { ingredients: [] } });
  };

  return (
    <div>
      <h1>오류</h1>
      <p>{message}</p>
      <button onClick={handleRetry}>다시 시도</button>
      <button onClick={handleManualCorrection}>수동으로 재료 추가</button>
    </div>
  );
}

export default ErrorPage;
