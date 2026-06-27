const map = L.map('map').setView([23.2599, 77.4126], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

let marker;

map.on("click", function(e){

    if(marker){
        map.removeLayer(marker);
    }

    marker = L.marker(e.latlng).addTo(map);

    document.getElementById("latitude").value = e.latlng.lat;
    document.getElementById("longitude").value = e.latlng.lng;

});
window.addEventListener("load",()=>{

    document.body.style.opacity="1";

});