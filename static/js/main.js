
var layers = {

    "Units":
    {"url": "/units.kml",
        "name": "units"},

    "LocalLoop":
    {"url": "https://maps.google.com/maps/ms?authuser=0&vps=2&ie=UTF8&msa=0&output=kml&msid=216496306373642223874.0004ac6f58b60f202649a",
        "name": "Current in use fiber"},



};

function initialize() {
    var macon = new google.maps.LatLng(32.834722, -83.651667);
    var mapOptions = {
        center: macon,
        zoom: 11,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);

    for(var layer in layers) {
        addOptionItem(layer, layers[layer].img, layers[layer].name);
        document.getElementById(layer).checked = true;
        toggleGeoXML(layer, true);

    }




}

function addOptionItem(id) {
    var layerOptions = document.createElement("div");

    var inputTD = document.createElement("div");
    inputTD.id = id + "div";
    inputTD.className = "OptionInputDiv";
    var input = document.createElement("input");
    input.type = "checkbox";
    input.id = id;
    input.className = "optioninput";
    input.onclick = function () { toggleGeoXML(this.id, this.checked) };
    inputTD.appendChild(input);

    var nameTD = document.createElement("div");
    nameTD.className = "optionnamediv";
    var nameA = document.createElement("a");
    nameA.href = layers[id].url;
    nameA.className = "optionnameLink";
    var name = document.createTextNode(layers[id].name);
    nameA.appendChild(name);
    nameTD.appendChild(nameA);


    layerOptions.appendChild(inputTD);
    layerOptions.appendChild(nameTD);
    document.getElementById("OptionMenu").appendChild(layerOptions);
}

function zoomToGeoXML(geoXml) {
    var center = geoXml.getDefaultCenter();
    var span = geoXml.getDefaultSpan();
    var sw = new GLatLng(center.lat() - span.lat() / 2,
        center.lng() - span.lng() / 2);
    var ne = new GLatLng(center.lat() + span.lat() / 2,
        center.lng() + span.lng() / 2);
    var bounds = new GLatLngBounds(sw, ne);
    map.setCenter(center);
    map.setZoom(map.getBoundsZoomLevel(bounds));
}

function toggleGeoXML(id, checked) {
    if (checked) {
        if (!layers[id].geoxml) {

            var geoXml = new google.maps.KmlLayer(layers[id].url, {preserveViewport: true})
            layers[id].geoXml = geoXml;
            geoXml.setMap(map);
            //map.addOverlay(layers[id].geoXml);
        }


    } else  {
        layers[id].geoXml.setMap(null);


    }
}








    $(document).ready(function() {



    });





