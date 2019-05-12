





require([
  "esri/Map",
  "esri/views/MapView",

  "esri/widgets/Search",

  "esri/layers/VectorTileLayer",

  "esri/widgets/Sketch",
  "esri/layers/GraphicsLayer",
  "esri/layers/FeatureLayer",
  "esri/layers/TileLayer",
  "esri/layers/WMTSLayer",
  "esri/layers/WMSLayer"


], function(Map, MapView, Search, VectorTileLayer, Sketch, GraphicsLayer, FeatureLayer, TileLayer, WMTSLayer, WMSLayer) {
  const base_layer = new GraphicsLayer();

  var map = new Map({
    basemap: "topo-vector"
  });
  map.add(base_layer);


  wind_layer = new TileLayer({
      url: "https://tiles.arcgis.com/tiles/Lhhlijt6OxVvJhC4/arcgis/rest/services/Wind_tile/MapServer"
  });

  map.add(wind_layer);
  wind_layer.visible = false;


  solar_layer = new TileLayer({
      url: "https://tiles.arcgis.com/tiles/Lhhlijt6OxVvJhC4/arcgis/rest/services/Map/MapServer"
  });

  map.add(solar_layer);
  solar_layer.visible = false;



  water_layer = new WMTSLayer({
    url: "https://storage.googleapis.com/global-surface-water/downloads_ancillary/WMTS_Global_Surface_Water.xml"
  });
  map.add(water_layer);
  water_layer.visible = false;



  energy_layer = new WMSLayer({
    url: "http://services.ga.gov.au/gis/services/Proximity_To_Transmission_Infrastructure_Lines_WM/MapServer/WMSServer"
    // sublayers: [{
    //   name: // name of the sublayer,
    //   legendUrl: // url to the legend
    // }]
  });
  map.add(energy_layer);
  energy_layer.visible = false;




  hydro_layer = new WMSLayer({
    url: "https://gis.aremi.data61.io/anu/wms"
  });
  map.add(hydro_layer);
  hydro_layer.visible = false;

  // const fl = new FeatureLayer({
  //   url: "https://tiles.arcgis.com/tiles/ryycKNjqBGg4M7N9/arcgis/rest/services/Wind_for_AU_NZ_ID_PNG_WTL1/MapServer/2a"
  //   });
  // map.add(fl);

  // <style>
  // .embed-container {
  //   position: relative;
  //   padding-bottom: 80%;
  //   height: 0; max-width: 100%;}
  // .embed-container iframe,
  // .embed-container object,
  // .embed-container iframe{
  //   position: absolute;
  //   top: 0;
  //   left: 0;
  //   width: 100%;
  //   height: 100%;}


  // small{
  //   position: absolute;
  //   z-index: 40;
  //   bottom: 0;
  //   margin-bottom: -15px;}
  // </style>
  // <div class="embed-container">
  //   <iframe width="500" height="400" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" title="Solar Insolation Map Global"
  //   src="//esrau.maps.arcgis.com/apps/Embed/index.html?webmap=2a38d472ceff42ceb5ea45a3dc29a878&extent=-180,-72.2486,180,72.9587&zoom=true&previewImage=false&scale=true&disable_scroll=true&theme=light">
  //   </iframe></div>

  var view = new MapView({
    container: "viewDiv",
    map: map,
    center: [147.71511,-36.09042],
    zoom: 3
  });

  var search = new Search({
  view: view
  });

  const sketch = new Sketch({
    layer: base_layer,
    view: view
    });

  view.ui.add(sketch, "top-right");

  view.ui.add(search, "top-right");

  view.on("click", function(evt){
  search.clear();
  view.popup.clear();
  if (search.activeSource) {
    var geocoder = search.activeSource.locator; // World geocode service
    geocoder.locationToAddress(evt.mapPoint)
      .then(function(response) { // Show the address found
        var address = response.address;
        showPopup(address, evt.mapPoint);
      }, function(err) { // Show no address found
        showPopup("No address found.", evt.mapPoint);
      });
  }
});


//   sketch.on("create", function(event) {
//   if (event.state === "complete") {

//     console.log(event.mapPoint.longitude);


//   }
// });


  

  function showPopup(address, pt) {
    view.popup.open({
      title:  + Math.round(pt.longitude * 100000)/100000 + "," + Math.round(pt.latitude * 100000)/100000,
      content: address,
      location: pt
    });

  }

  // // Listen to sketch widget's create event.
  // sketch.on("create", function(event) {
  //   // check if the create event's state has changed to complete indicating
  //   // the graphic create operation is completed.
  //   if (event.state === "complete") {
  //     // remove the graphic from the layer. Sketch adds
  //     // the completed graphic to the layer by default.
  //     polygonGraphicsLayer.remove(event.graphic);

  //     // use the graphic.geometry to query features that intersect it
  //     selectFeatures(event.graphic.geometry);
  //   }
  // });



});