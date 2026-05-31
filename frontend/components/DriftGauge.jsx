import React, { useEffect, useRef } from "react";
import Chart from "chart.js/auto";

const DriftGauge = ({ driftScore }) => {
  const chartRef = useRef(null);

  useEffect(() => {
    if (!driftScore) return;

    const ctx = chartRef.current.getContext("2d");

    new Chart(ctx, {
      type: "doughnut",
      data: {
        datasets: [
          {
            data: [driftScore * 100, 100 - driftScore * 100],
            backgroundColor: ["#ff4d4d", "#1a1a1a"],
            borderWidth: 0
          }
        ]
      },
      options: {
        cutout: "80%",
        plugins: {
          tooltip: { enabled: false }
        }
      }
    });
  }, [driftScore]);

  return (
    <div className="gauge-box">
      <h3>🔁 Model Drift Score</h3>
      <canvas ref={chartRef}></canvas>
      <p>{(driftScore * 100).toFixed(2)}%</p>
    </div>
  );
};

export default DriftGauge;