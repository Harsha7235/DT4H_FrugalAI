import React, { useEffect, useState } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Legend,
  ResponsiveContainer
} from "recharts";

const OrganTimelineChart = ({ patientName }) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    if (!patientName) return;

    fetch(`http://127.0.0.1:8000/organ_timeline/${patientName}`)
      .then(res => res.json())
      .then(res => {
        const formatted = res.map((item, index) => ({
          index: index + 1,
          heart: item.heart,
          liver: item.liver,
          pancreas: item.pancreas,
          kidney: item.kidney,
          damage: item.cumulative_damage
        }));
        setData(formatted);
      });
  }, [patientName]);

  return (
    <div className="chart-box">
      <h3>🧬 Organ Damage Over Time</h3>
      <ResponsiveContainer width="100%" height={350}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="index" />
          <YAxis domain={[0, 100]} />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="heart" stroke="#ff4d4d" />
          <Line type="monotone" dataKey="liver" stroke="#ffa500" />
          <Line type="monotone" dataKey="pancreas" stroke="#00ccff" />
          <Line type="monotone" dataKey="kidney" stroke="#66ff66" />
          <Line type="monotone" dataKey="damage" stroke="#ffffff" strokeWidth={3} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default OrganTimelineChart;