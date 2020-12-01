let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 43.0389, lng: -87.906 },
    zoom: 8,
  });
}

function markerArray(list, map){
  res = []
  for (l of list){
    m = makeMarker(l.latitude, l.longitude,map)
    res.push({weight:l.weight, marker:m})
  }
  return res
}

function makeMarker(latitude,longitude, map){
  p = {lat: latitude, lng:longitude}
  args = {position: p, map};
  return new google.maps.Marker(args);
}

function makeWeightedLocation(lat,long,w){
  var loc = new google.maps.LatLng(lat, long);
  return {location: loc, weight: w};
}

function makeWeightedLocationList(list) {
  retval = []
  for (l of list) {
    retval.push(makeWeightedLocation(l.latitude, l.longitude, l.weight));
  }
  return retval;
}