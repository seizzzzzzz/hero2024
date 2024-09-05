// frontend/diabetes-recipe-app/src/pages/UploadPage.js

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function UploadPage() {
  const [image, setImage] = useState(null);
  const navigate = useNavigate();

  const handleImageUpload = (event) => {
    setImage(event.target.files[0]);
  };

  const handleIngredientDetection = async () => {
    if (!image) {
      navigate('/error', { state: { message: "이미지를 업로드해주세요." } });
      return;
    }

    const formData = new FormData();
    formData.append('image', image);

    try {
      const response = await fetch('/api/upload/', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error("이미지 인식 중 오류가 발생했습니다.");
      }

      const data = await response.json();
      if (data.ingredients.length === 0) {
        navigate('/error', { state: { message: "적합하지 않은 사진입니다." } });
      } else {
        navigate('/ingredients', { state: { ingredients: data.ingredients } });
      }
    } catch (err) {
      navigate('/error', { state: { message: err.message } });
    }
  };

  return (
    <div className="upload-container">
      <h1>이미지 업로드</h1>
      <input type="file" onChange={handleImageUpload} />
      <button onClick={handleIngredientDetection}>재료 인식</button>
    </div>
  );
}

export default UploadPage;
