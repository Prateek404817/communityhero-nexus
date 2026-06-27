const map = L.map("map").setView([23.2599, 77.4126], 13);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "&copy; OpenStreetMap contributors"
}).addTo(map);

let marker = null;

map.on("click", function (e) {

    if (marker) {
        map.removeLayer(marker);
    }

    marker = L.marker(e.latlng).addTo(map);

    const latInput = document.getElementById("latitude");
    const lngInput = document.getElementById("longitude");

    latInput.value = e.latlng.lat;
    lngInput.value = e.latlng.lng;

    console.log("Latitude:", latInput.value);
    console.log("Longitude:", lngInput.value);
});