import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [spotPrice, setSpotPrice] = useState(100);
  const [strikePrice, setStrikePrice] = useState(100);
  const [riskFreeRate, setRiskFreeRate] = useState(0.05);
  const [volatility, setVolatility] = useState(0.2);
  const [timeToMaturity, setTimeToMaturity] = useState(1);
  const [quoteDetails, setQuoteDetails] = useState('');

  console.log("TEsT")

  const createQuoteRequest = async () => {
    try {
      const response = await axios.post('https://localhost:5001/api/QuoteRequest/create-option', {
        spotPrice,
        strikePrice,
        riskFreeRate,
        volatility,
        timeToMaturity
      });
      setQuoteDetails(response.data);
    } catch (error) {
      console.error('There was an error creating the quote request!', error);
    }
  };

  return (
    <div className="App">
      <h1>Option Quote Request</h1>
      <div className="form-group">
        <label>Spot Price:</label>
        <input type="number" value={spotPrice} onChange={(e) => setSpotPrice(e.target.value)} />
      </div>
      <div className="form-group">
        <label>Strike Price:</label>
        <input type="number" value={strikePrice} onChange={(e) => setStrikePrice(e.target.value)} />
      </div>
      <div className="form-group">
        <label>Risk-Free Rate:</label>
        <input type="number" step="0.01" value={riskFreeRate} onChange={(e) => setRiskFreeRate(e.target.value)} />
      </div>
      <div className="form-group">
        <label>Volatility:</label>
        <input type="number" step="0.01" value={volatility} onChange={(e) => setVolatility(e.target.value)} />
      </div>
      <div className="form-group">
        <label>Time to Maturity:</label>
        <input type="number" step="0.01" value={timeToMaturity} onChange={(e) => setTimeToMaturity(e.target.value)} />
      </div>
      <button onClick={createQuoteRequest}>Create Quote Request</button>
      {quoteDetails && (
        <div className="result">
          <strong>Quote Details:</strong> {quoteDetails}
        </div>
      )}
    </div>
  );
}

export default App;
