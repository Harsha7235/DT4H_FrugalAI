import React, { useEffect, useRef } from "react";
import Chart from "chart.js/auto";

const ShapHeatmap = ({ shapValues }) => {
  const chartRef = useRef(null);

  useEffect(() => {
    if (!shapValues) return;

    const ctx = chartRef.current.getContext("2d");

    new Chart(ctx, {
      type: "bar",
      data: {
        labels: Object.keys(shapValues),
        datasets: [
          {
            label: "SHAP Impact",
            data: Object.values(shapValues),
            backgroundColor: "#ff6384"
          }
        ]
      }
    });
  }, [shapValues]);

  return (
    <div className="chart-box">
      <h3>🧠 SHAP Explainability</h3>
      <canvas ref={chartRef}></canvas>
    </div>
  );
};

export default ShapHeatmap;