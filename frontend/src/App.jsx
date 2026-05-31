import React, { useEffect, useState } from "react";
import "./App.css";
import axios from "axios";

import loaderImg from "./assets/loader.png";
import twinVideo from "./assets/twin.mp4";

import HumanModel from "./components/HumanModel";

import {
LineChart,
Line,
XAxis,
YAxis,
Tooltip,
ResponsiveContainer,
BarChart,
Bar
} from "recharts";

const safeArray = (d) => Array.isArray(d) ? d : [];

const safeObjectToArray = (obj) =>
obj && typeof obj === "object"
? Object.entries(obj).map(([k,v]) => ({
name:k,
value:Number(v)||0
}))
: [];

function App(){

const [bootLoading,setBootLoading] = useState(true);
const [assetsLoaded,setAssetsLoaded] = useState(false);
const [loading,setLoading] = useState(false);
const [result,setResult] = useState(null);
const [timeline,setTimeline] = useState([]);
const [showAnatomy,setShowAnatomy] = useState(false);

const [form,setForm] = useState({
name:"",
age:"",
bmi:"",
bp:"",
glucose:"",
cholesterol:"",
smoking:"",
dose:"",
tablets:"",
days:""
});

useEffect(()=>{
const timer=setTimeout(()=>setBootLoading(false),2500);
return ()=>clearTimeout(timer);
},[]);

useEffect(()=>{
const v=document.createElement("video");
v.src=twinVideo;
v.onloadeddata=()=>setAssetsLoaded(true);
},[]);

const handleChange=(e)=>{
setForm({
...form,
[e.target.name]:e.target.value
})
}

const limits={
age:[0,120],
bmi:[10,60],
bp:[70,250],
glucose:[50,500],
cholesterol:[100,400],
dose:[0,2000],
tablets:[0,20],
days:[1,365]
}

const allValid=
Object.keys(limits).every(k=>{
const v=Number(form[k])
return v>=limits[k][0] && v<=limits[k][1]
})
&& form.name!=="" 
&& form.smoking!=="";

useEffect(() => {

if(!allValid) return;

let ignore=false;

async function runPrediction(){

if(ignore) return;

try{

setLoading(true)

const response = await axios.post(
"http://127.0.0.1:8000/predict",
{
name:form.name,
age:Number(form.age),
bmi:Number(form.bmi),
bp:Number(form.bp),
glucose:Number(form.glucose),
cholesterol:Number(form.cholesterol),
smoking:form.smoking,
dose:Number(form.dose),
tablets:Number(form.tablets),
days:Number(form.days)
})

if(!ignore){
setResult(response.data)
}

}catch(err){
console.error(err)
}

setLoading(false)

}

runPrediction()

return ()=>{ ignore=true }

},[
form.name,
form.age,
form.bmi,
form.bp,
form.glucose,
form.cholesterol,
form.smoking,
form.dose,
form.tablets,
form.days
])

if(bootLoading){

return(

<div className="boot-loader">

<img src={loaderImg} className="loading-img" alt="" />

<div className="boot-spinner"></div>

<h2>Initializing Autonomous Digital Twin...</h2>

</div>

)

}

const organData=safeObjectToArray(result?.organ_stress)
const pkpdData=safeArray(result?.pkpd_simulation)
const progressionData=safeArray(result?.progression)
const monteData=safeArray(result?.monte_carlo)
const heatmapData=safeArray(result?.ai_heatmap)

return(

<div className="container">

<div className="left">

<h1 className="title">Autonomous Digital Twin</h1>

<div className="input-group">
<label>Name</label>
<input
name="name"
value={form.name}
onChange={handleChange}
/>
</div>

{Object.keys(limits).map(key=>{

const[min,max]=limits[key]
const val=form[key]

const warn=val && (val<min || val>max)

return(

<div className="input-group" key={key}>

<label>{key.toUpperCase()} ({min}-{max})</label>

<input
name={key}
value={val}
onChange={handleChange}
className={warn?"input-warn":""}
/>

{warn && <div className="range-warning">Out of safe range</div>}

</div>

)

})}

<div className="input-group">

<label>Smoking</label>

<select
name="smoking"
value={form.smoking}
onChange={handleChange}
>

<option value="">Select</option>
<option value="Non-Smoker">Non-Smoker</option>
<option value="Smoker">Smoker</option>

</select>

</div>

</div>

<div className="right">

{!allValid && assetsLoaded && (

<div className="twin-preview">

<video
className="video-full"
src={twinVideo}
autoPlay
loop
muted
/>

<div className="twin-description">

<h2>Autonomous Digital Twin</h2>

<p>
AI digital twin simulates organ interactions,
drug pharmacokinetics, disease progression,
and biological damage.
</p>

</div>

</div>

)}

{loading && (

<div className="full-loader">

<div className="spinner"></div>

<h2>Running Simulation…</h2>

</div>

)}

{result && !loading && (

<>

<button
className="anatomy-btn"
onClick={()=>setShowAnatomy(!showAnatomy)}
>

{showAnatomy ? "Back Twin" : "Show Anatomy"}

</button>

{showAnatomy && (

<div className="anatomy-panel">

<div className="anatomy-model">
<HumanModel stress={result.organ_stress}/>
</div>

<div className="organ-values">

<h2>Organ Stress</h2>

<p>Heart: {result?.organ_stress?.heart?.toFixed(2)}</p>
<p>Liver: {result?.organ_stress?.liver?.toFixed(2)}</p>
<p>Pancreas: {result?.organ_stress?.pancreas?.toFixed(2)}</p>
<p>Kidney: {result?.organ_stress?.kidney?.toFixed(2)}</p>

</div>

</div>

)}

{!showAnatomy && (

<div className="dashboard">

<div className="section">

<h2>Risk Probability</h2>

<h1>{((result.probability||0)*100).toFixed(2)}%</h1>

<p>Tier: {result.tier}</p>

</div>

<div className="section">

<h2>Biomarkers</h2>

<p>ALT: {result?.biomarkers?.ALT}</p>
<p>AST: {result?.biomarkers?.AST}</p>
<p>Creatinine: {result?.biomarkers?.Creatinine}</p>
<p>Troponin: {result?.biomarkers?.Troponin}</p>

</div>

<div className="section">

<h2>Organ Stress</h2>

<ResponsiveContainer width="100%" height={220}>

<BarChart data={organData}>
<XAxis dataKey="name"/>
<YAxis/>
<Tooltip/>
<Bar dataKey="value" fill="#00eaff"/>
</BarChart>

</ResponsiveContainer>

</div>

<div className="section">

<h2>Drug PK/PD</h2>

<ResponsiveContainer width="100%" height={220}>

<LineChart data={pkpdData}>
<XAxis dataKey="time"/>
<YAxis/>
<Tooltip/>
<Line type="monotone" dataKey="concentration" stroke="#00ff88" strokeWidth={3} dot={false}/>
</LineChart>

</ResponsiveContainer>

</div>

<div className="section">

<h2>Disease Progression</h2>

<ResponsiveContainer width="100%" height={220}>

<LineChart data={progressionData}>
<XAxis dataKey="time"/>
<YAxis/>
<Tooltip/>
<Line type="monotone" dataKey="risk" stroke="#ff4c4c" strokeWidth={3} dot={false}/>
</LineChart>

</ResponsiveContainer>

</div>

<div className="section">

<h2>Risk Distribution</h2>

<ResponsiveContainer width="100%" height={220}>

<LineChart data={monteData}>
<XAxis dataKey="iteration"/>
<YAxis/>
<Tooltip/>
<Line type="monotone" dataKey="risk" stroke="#00eaff" strokeWidth={2} dot={false}/>
</LineChart>

</ResponsiveContainer>

</div>

<div className="section">

<h2>AI Explainability</h2>

<ResponsiveContainer width="100%" height={220}>

<BarChart data={heatmapData}>
<XAxis dataKey="feature"/>
<YAxis/>
<Tooltip/>
<Bar dataKey="impact" fill="#ff4c4c"/>
</BarChart>

</ResponsiveContainer>

</div>

<div className="section">

<h2>Model Learning</h2>

<p>Dataset Size: {result?.model_learning?.dataset_size}</p>
<p>Model: {result?.model_learning?.model}</p>
<p>Confidence: {result?.model_learning?.confidence}%</p>

<ul>
{result?.model_learning?.top_features?.map((f,i)=>(
<li key={i}>{f}</li>
))}
</ul>

</div>

</div>

)}

</>

)}

</div>

</div>

)

}

export default App;