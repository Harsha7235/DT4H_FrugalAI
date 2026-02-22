import { useState } from "react";
import axios from "axios";

function HealthForm({ setResult }) {
  const [form, setForm] = useState({
    age: "",
    bmi: "",
    bp: "",
    glucose: "",
    cholesterol: "",
    sleep_hours: ""
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: Number(e.target.value) });
  };

  const handleSubmit = async () => {
    const res = await axios.post("http://127.0.0.1:8000/predict", form);
    setResult(res.data);
  };

  return (
    <div className="grid grid-cols-2 gap-4">
      {Object.keys(form).map((key) => (
        <input
          key={key}
          name={key}
          placeholder={key}
          onChange={handleChange}
          className="p-2 rounded bg-gray-700 border border-gray-600"
        />
      ))}

      <button
        onClick={handleSubmit}
        className="col-span-2 bg-blue-500 hover:bg-blue-600 p-2 rounded mt-2"
      >
        Predict Risk
      </button>
    </div>
  );
}

export default HealthForm;