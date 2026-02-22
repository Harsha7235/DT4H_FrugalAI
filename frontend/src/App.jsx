import { useState } from "react";
import HealthForm from "./components/HealthForm";
import RiskChart from "./components/RiskChart";
import Chatbot from "./components/Chatbot";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center p-8">
      <h1 className="text-4xl font-bold mb-6 text-blue-400">
        Autonomous Digital Twin Healthcare
      </h1>

      <div className="bg-gray-800 p-6 rounded-xl shadow-xl w-full max-w-3xl">
        <HealthForm setResult={setResult} />
      </div>

      {result && (
        <div className="bg-gray-800 p-6 rounded-xl shadow-xl w-full max-w-3xl mt-6">
          <h2 className="text-xl font-semibold mb-2">
            Risk Probability: {result.risk_probability.toFixed(2)}
          </h2>
          <p className="mb-4">{result.risk_level}</p>
          <RiskChart risk={result.risk_probability} />
        </div>
      )}

      <div className="bg-gray-800 p-6 rounded-xl shadow-xl w-full max-w-3xl mt-6">
        <Chatbot />
      </div>
    </div>
  );
}

export default App;