
import React, { useEffect, useState } from 'react'
import Graph from 'react-vis-network-graph'
import data from "../Test/Graph.json";
import Nodes from '../Test/Nodes.json'

function Node ( id , title , shape , color ){
    this.id = id;
    this.title = title;
    this.shape = shape;
    this.color = color;
}

function GraphView() {
    const [nodes, setNodes] = useState(true);

    function preTitle(text) {
        const container = document.createElement("pre");
        container.innerText = text;
        return container;
    }

    function getJSON(){
        data.map((x) => (
            console.log(x)
            
        ))
        
    }

    function getNodes(){
        //var Nodos = []
        Nodes.map((x) => (
            console.log(x.id)
            //setNodes(x)
        ))
        //console.log(Nodos)
        //console.log(Nodos[0])
        //return Nodos;
    }



    function Test(){
        console.log("Test");
    }

    useEffect(() => {
        console.log("Render!!");
        Test();
        getJSON();
        getNodes();
        const updateNode = () => {
            setNodes(false)
        }
        updateNode();
    });

    var Node1 =  { id : 126505 , title: preTitle("MRAutor:126505\nNombre: Montejano-Peimbert, Luis\nGender: male\nActivity Since: 1974\nTotal Publications: 110"), shape: "circle", color: "#6499E9"}
    var Node2 = { id : 70670 , title: preTitle("MRAutor:70670\nNombre: Galeana-Sánchez, Hortensia\nGender: female\nActivity Since: 1982\nTotal Publications: 159"), shape: "circle", color: "#D988B9"}
    const graph = {
        nodes : [
            Node1,
            Node2,
            { id : 176235 , title: preTitle("MRAutor:176235\nNombre: Urrutia, Jorge, Hortensia\nGender: male\nActivity Since: 1980\nTotal Publications: 202"), shape: "circle", color: "#6499E9"}
        ],
        edges : [
            
            {from: 126505 , to: 70670},
            {from: 70670 , to: 176235}
        ]
    }
    const options = {
        interaction: {
            navigationButtons: true
        },
        nodes: {
            borderWidth: 2, //Check
            size: 40,
            color: {
                border: "white",
                background: "#666666"
            },
            font: {
                color: "white"
            }
        },
        edges: {
            arrows: '', //No tienen flechas alguna
            color: "white"
        },
        shadow: true,
        smooth: true,
        height: "500px" //900px
    }

  return (
      <div className='container'> 
        <Graph 
            graph = {graph}
            options = {options}
        />
      </div>
    
  )
}

export default GraphView
