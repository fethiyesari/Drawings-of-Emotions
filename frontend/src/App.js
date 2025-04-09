import React, { useState } from 'react';

function App() {
  const [image, setImage] = useState(null);
  const [result, setResult] = useState(null);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(URL.createObjectURL(file));
    }
  };

  const handleAnalyze = () => {
    // Burada backend'e çağrı yapıp sonucu alacağız
    setResult("Çizim başarılı bir şekilde analiz edildi! (Sonuçlar gelecek)");
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gradient-to-r from-purple-500 via-pink-500 to-red-500">
    <div className="bg-white p-8 rounded-xl shadow-lg max-w-lg w-full">
    <h1 className="text-4xl font-bold text-gray-800 mb-6 text-center">Çizim Duygusal Durum Analizi</h1>
    <div className="text-4xl text-red-500">Tailwind Test</div>

    {/* Resim Yükleme */}
    <div className="mb-4">
      <input
        type="file"
        accept="image/*"
        onChange={handleImageChange}
        className="file-input file-input-bordered file-input-primary w-full text-gray-700 py-2 px-4 border-2 rounded-md"
      />
    </div>
    
    {/* Yüklenen Resmi Göster */}
    {image && <img src={image} alt="Uploaded" className="max-w-xs mb-4 mx-auto border-2 border-gray-200 rounded-lg shadow-md" />}
    
    {/* Analiz Butonu */}
    <button
      onClick={handleAnalyze}
      className="w-full py-2 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition duration-300 ease-in-out transform hover:scale-105"
    >
      Analiz Et
    </button>

    {/* Sonuç */}
    {result && <p className="mt-6 text-xl text-gray-800 text-center">{result}</p>}
  </div>
</div>
  );
}

export default App;
