import React, { Component } from 'react';
import './App.css';
import L from 'leaflet';
import { Map, TileLayer, Marker, Popup} from 'react-leaflet';
import leafGreen from './assets/leaf-green.png';
import leafRed from './assets/leaf-red.png';
import leafOrange from './assets/leaf-orange.png';
import leafShadow from './assets/leaf-shadow.png';
import { specimenData } from "./assets/specimen";
import { useState, useEffect, useRef } from "react";


export default function App() {


  const state = {
    greenIcon: {
      lat: 27.7172,
      lng: 85.3240,
    },
    redIcon: {
      lat: 27.1772,
      lng: 85.3240,
    },
    orangeIcon: {
      lat: 27.4572,
      lng: 85.4560,
    },
    zoom: 13
  }
  const lati = 27.7172
  const lng = 85.3240
  const mapRef = useRef(null);
  const [position, setPosition] = useState({
    lat: 27.7172,
    lng: 85.3240,
  });

  function handleLoad(map) {
    mapRef.current = map;
  }

  function handleCenter() {
    if (!mapRef.current) return;

    const newPos = mapRef.current.getCenter().toJSON();
    setPosition(newPos);
  }
  //constcenter = { lat: 100, lng: 100 }



  // const grenIcon = L.icon({
  //   iconUrl: leafGreen,
  //   shadowUrl: leafShadow,
  //   iconSize: [38, 95], // size of the icon
  //   shadowSize: [50, 64], // size of the shadow
  //   iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
  //   shadowAnchor: [4, 62],  // the same for the shadow
  //   popupAnchor: [-3, -76]
  // });

  // const redIcon = L.icon({
  //   iconUrl: leafRed,
  //   shadowUrl: leafShadow,
  //   iconSize: [38, 95], // size of the icon
  //   shadowSize: [50, 64], // size of the shadow
  //   iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
  //   shadowAnchor: [4, 62],  // the same for the shadow
  //   popupAnchor: [-3, -86]
  // });
  const [icons, setIcons] = useState(L.icon({
    iconUrl: "https://i.ibb.co/vssfpvY/icons8-dna-48.png",
    iconSize: [38, 95], // size of the icon
    iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
    popupAnchor: [-100, -100]
  }));

  const markerIcon = new L.Icon({
    iconUrl: "https://www.freeiconspng.com/img/39480",
    iconSize: [40, 40],
    iconAnchor: [17, 46], //[left/right, top/bottom]
    popupAnchor: [0, -46], //[left/right, top/bottom]
  });

  // const specimenIcon = L.Icon({
  //   iconUrl: "https://i.ibb.co/vssfpvY/icons8-dna-48.png",
  //   iconSize: [38, 95], // size of the icon
  //   iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
  //   popupAnchor: [-3, -86]
  // });


  const [selectedPark, setSelectedPark] = useState(null);
  // const positionRedIcon = [this.state.redIcon.lat, this.state.redIcon.lng];
  // const positionGreenIcon = [this.state.GreenIcon.lat, this.state.GreenIcon.lng];
  // const positionOrangeIcon = [this.state.orangeIcon.lat, this.state.orangeIcon.lng];
  // useEffect(() => {
  //   const listener = e => {
  //     if (e.key === "Escape") {
  //       setSelectedPark(null);
  //     }
  //   };
  //   window.addEventListener("keydown", listener);

  //   return () => {
  //     window.removeEventListener("keydown", listener);
  //   };
  // }, []);

  const [markers, setMarkers] = useState(null);
  return (
    <Map className="maps" center={position} zoom={13}>
      <TileLayer
        attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {specimenData.map(park => (
        <Marker
          key={park.record_id}
          //icon= specimenIcon.addTo(map)
          position={{
            lat: parseFloat(park.lat),
            lng: parseFloat(park.lon),
          }}
          
          icon = {icons}
          
        //longitude={parseFloat(park.lon)}
        //latitude={parseFloat(park.lat)}
        >
          <button
            className="marker-btn"
            onClick={e => {
              e.preventDefault();
              setSelectedPark(park);
            }}
          >
            {/* <img src={require('../assets/icons8-dna-48.png').default} alt="DNA Icon" /> */}
            <img src="https://i.ibb.co/vssfpvY/icons8-dna-48.png" alt="icons8-dna-48" />
          </button>
          <Popup maxWidth="auto" maxHeight="auto"
          onClick={e => {
            e.preventDefault();
            setSelectedPark(park);
          }}
            onClose={() => {
              setSelectedPark(null);
            }}
          >
            <div>
              <h2>{park.phylum}</h2>
              <p>{"Class: " + park.class_name}</p>
              <p>{"Order: " + park.order_name}</p>
              <p>{"BIN ID: " +park.bin_url}</p>
              <p>{"Country: " +park.country}</p>
              <p>{"Field Number: " +park.fieldnum}</p>
              <p>{"Identification Provided By: " +park.identification_provided_by}</p>             
              <p>{"Sex: " +park.sex}</p>
              <p>{"Marker Code: " +park.markercode}</p>
              <p>{"Life Stage: " +park.lifestage}</p>
              <p>{"Coordinates: " +park.geo_location}</p>
            </div>
          </Popup>
        </Marker>
      ))}

      {/* <Marker position={positionGreenIcon} icon={this.grenIcon}>
        <Popup>
          I am a green leaf
        </Popup>
      </Marker>
      <Marker position={positionRedIcon} icon={this.redIcon}>
        <Popup>
          I am a red leaf
        </Popup>
      </Marker>
      <Marker position={positionOrangeIcon} icon={this.orangeIcon}>
        <Popup>
          I am an orange leaf
        </Popup>
      </Marker> */}
        {selectedPark ? (
          <Popup maxWidth="auto" maxHeight="auto"
          position={{
            lat: parseFloat(selectedPark.lat),
            lng: parseFloat(selectedPark.lon),
          }}
            onClose={() => {
              setSelectedPark(null);
            }}
          >
            
            <div>
              <h2>{selectedPark.phylum}</h2>
              <p>{selectedPark.order_name}</p>
              <p>{selectedPark.nucleotides}</p>
              <p>{selectedPark.lifestage}</p>
            </div>
          </Popup>
        ) : null}

      {/* {markers.map((marker, i) => (
        <Marker key={`marker-${i}`} position={marker}>
          <Popup>
            <span>
              A pretty CSS3 popup. <br /> Easily customizable.
            </span>
          </Popup>
        </Marker>
      ))} */}
    </Map>
  );
}


