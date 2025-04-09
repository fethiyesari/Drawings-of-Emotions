import React, { useState } from 'react';
import { Button, Container, Card, CardBody, CardTitle } from 'reactstrap';

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
    setResult("Çizim başarılı bir şekilde analiz edildi! (Sonuçlar gelecek)");
  };

  return (
    <Container className="d-flex justify-content-center align-items-center vh-100">
      <Card className="p-4 shadow-lg hover:shadow-2xl transition duration-300 ease-in-out" style={{ maxWidth: '500px', width: '100%' }}>

        <CardBody>
        <CardTitle tag="h1" className="text-center animate__animated animate__fadeIn animate__delay-1s">
          Drawings of Emotions
        </CardTitle>

          <input
            type="file"
            accept="image/*"
            onChange={handleImageChange}
            className="form-control mb-4"
          />
          {image && <img src={image} alt="Uploaded" className="img-fluid mb-4 mx-auto" />}
          <Button onClick={handleAnalyze} color="primary" block className="transition duration-300 transform hover:scale-105">
            <i className="fa fa-magic"></i> Analiz Et
          </Button>
          {result && <p className="mt-4 text-center">{result}</p>}
        </CardBody>
      </Card>
    </Container>
  );
}

export default App;
