import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement } from "chart.js";

ChartJS.register(CategoryScale, LinearScale, BarElement);

function RiskChart({ risk }) {
  return (
    <Bar
      data={{
        labels: ["Risk Score"],
        datasets: [
          {
            label: "Risk",
            data: [risk],
          },
        ],
      }}
    />
  );
}

export default RiskChart;