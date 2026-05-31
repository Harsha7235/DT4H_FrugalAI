import React, { Suspense, useRef, useEffect } from "react"
import { Canvas, useFrame } from "@react-three/fiber"
import { OrbitControls, useGLTF } from "@react-three/drei"
import * as THREE from "three"

/* -----------------------------
   AI HEATMAP COLOR FUNCTION
--------------------------------*/

function heatColor(v){

if(v < 0.4) return "#2ecc71"
if(v < 0.7) return "#f1c40f"
return "#ff0000"

}

/* -----------------------------
   HUMAN MODEL
--------------------------------*/

function Model({ stress }) {

const safeStress = {
heart: stress?.heart ?? 0,
liver: stress?.liver ?? 0,
pancreas: stress?.pancreas ?? 0,
kidney: stress?.kidney ?? 0
}

const { scene } = useGLTF("/models/HumanBody/Anatomy.glb")

const heartRef = useRef()

useEffect(() => {

scene.traverse((child) => {

if (child.isMesh || child.isSkinnedMesh) {

const name = child.name.toLowerCase()
const parent = child.parent?.name?.toLowerCase() || ""

console.log("Mesh:", name, "Parent:", parent)

/* HEART */

if (parent.includes("heart")) {

heartRef.current = child

child.material = child.material.clone()

child.material.color = new THREE.Color(heatColor(safeStress.heart))
child.material.emissive = new THREE.Color("red")
child.material.emissiveIntensity = safeStress.heart * 3

}

/* LIVER */

if (parent.includes("liver")) {

child.material = child.material.clone()

child.material.color = new THREE.Color(heatColor(safeStress.liver))
child.material.emissive = new THREE.Color("orange")
child.material.emissiveIntensity = safeStress.liver * 3

}

/* PANCREAS */

if (parent.includes("pancreas")) {

child.material = child.material.clone()

child.material.color = new THREE.Color(heatColor(safeStress.pancreas))
child.material.emissive = new THREE.Color("yellow")
child.material.emissiveIntensity = safeStress.pancreas * 3

}

/* KIDNEY */

if (parent.includes("kidney")) {

child.material = child.material.clone()

child.material.color = new THREE.Color(heatColor(safeStress.kidney))
child.material.emissive = new THREE.Color("purple")
child.material.emissiveIntensity = safeStress.kidney * 3

}

/* BRAIN */

if (parent.includes("brain")) {

child.material.color = new THREE.Color("#ff66ff")
child.material.emissive = new THREE.Color("#ff66ff")
child.material.emissiveIntensity = 0.5

}

/* ARTERIES */

if (parent.includes("arter")) {

child.material = child.material.clone()

child.material.color = new THREE.Color(
safeStress.heart > 0.7 ? "#ff0000" : "#ffaa00"
)

}

}

})

}, [scene, safeStress])

/* HEARTBEAT */

useFrame(({ clock }) => {

if (heartRef.current) {

const t = clock.getElapsedTime()

const speed = 3 + safeStress.heart * 8
const beat = 1 + Math.sin(t * speed) * 0.05

heartRef.current.scale.set(beat, beat, beat)

}

})

return (
<primitive object={scene} scale={2} position={[0, -135, 0]} />
)

}

/* -----------------------------
   ARTERY BLOOD FLOW
--------------------------------*/

function ArteryFlow() {

const lineRef = useRef()

const points = []

for (let i = -1.5; i < 1.5; i += 0.05) {

points.push(new THREE.Vector3(0, i, 0))

}

const geometry = new THREE.BufferGeometry().setFromPoints(points)

useFrame(({clock}) => {

if(lineRef.current){
lineRef.current.rotation.y =
clock.getElapsedTime() * 0.3
}

})

return (

<line ref={lineRef} geometry={geometry}>

<lineBasicMaterial color="red"/>

</line>

)

}

/* -----------------------------
   DRUG DIFFUSION WAVE
--------------------------------*/

function DrugWave() {

const wave = useRef()

useFrame(({clock}) => {

if(wave.current){

const t = clock.getElapsedTime()
const scale = 1 + Math.sin(t*2)*0.1

wave.current.scale.set(scale,scale,scale)

}

})

return (

<mesh ref={wave} position={[0,-200,0]}>

<sphereGeometry args={[0.6,32,32]}/>

<meshBasicMaterial
color="cyan"
wireframe
transparent
opacity={0.4}
/>

</mesh>

)

}

/* -----------------------------
   MAIN COMPONENT
--------------------------------*/

export default function HumanModel({ 
stress = { heart:0, liver:0, pancreas:0, kidney:0 } 
}) {

return (

<div style={{ width: "100%", height: "100%" }}>

<Canvas camera={{ position: [0, 1, 5], fov: 50 }}>

<ambientLight intensity={2} />
<directionalLight position={[5,5,5]} intensity={2} />

<Suspense fallback={null}>

<Model stress={stress} />

<ArteryFlow />

<DrugWave />

</Suspense>

<OrbitControls />

</Canvas>

</div>

)

}