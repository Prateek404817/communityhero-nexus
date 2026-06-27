let heatMap;

function loadHeatMap(points){

    if(!document.getElementById("heatmap")){
        return;
    }

    heatMap = L.map("heatmap").setView([23.2599,77.4126],12);

    L.tileLayer(
        "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        {
            attribution:"OpenStreetMap"
        }
    ).addTo(heatMap);

    points.forEach(point=>{

        let color="green";

        if(point.severity==="Medium")
            color="orange";

        if(point.severity==="High")
            color="red";

        L.circleMarker(
            [point.lat,point.lng],
            {
                radius:10,
                color:color,
                fillOpacity:0.8
            }
        ).addTo(heatMap);

    });

}