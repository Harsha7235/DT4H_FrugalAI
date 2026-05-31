import React from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const ResilienceChart = ({ age }) => {
  const resilience = Math.max(0.85 - age / 200, 0.5);

  const data = [
    { name: "Resilience", value: resilience * 100 }
  ];

  return (
    <div className="chart-box">
      <h3>🫀 Organ Resilience</h3>
      <ResponsiveContainer width="100%" height={250}>
        <BarChart data={data}>
          <XAxis dataKey="name" />
          <YAxis domain={[0, 100]} />
          <Tooltip />
          <Bar dataKey="value" fill="#00ffaa" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default ResilienceChart;