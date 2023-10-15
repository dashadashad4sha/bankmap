mapboxgl.accessToken = 'pk.eyJ1IjoiaGVsLWNvbiIsImEiOiJjbG5ibmcxMDYwNW9hMmp0ZGJoNGYyMDMyIn0.50UhRbmj4oxhJPuoyIUBcg';
      const map = new mapboxgl.Map({
          container: 'map',
          // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
          style: 'mapbox://styles/hel-con/clnoyx33400ck01pl0qh2d0dk',
          center: [37.570042, 55.419247], // lng, lat
          zoom: 16,
      });
      function getData(http_link) {
          return new Promise((resolve, reject) => {
              fetch(http_link)
                  .then(response => response.json())
                  .then(banks => resolve(banks))
                  .catch(err => reject);
          });
      }

function BuildNavigation(http_link) {
  getData(http_link).then(banks => {
      map.on('load', () => {
          if (navigator.geolocation) {
              navigator.geolocation.getCurrentPosition(function (position) {
                  var latitude = position.coords.latitude;
                  var longitude = position.coords.longitude;

                  var directions = new MapboxDirections({
                      accessToken: mapboxgl.accessToken,
                      unit: 'metric',
                      profile: 'walking'
                  });

                  map.addControl(directions, 'top-left');

                  directions.setOrigin([latitude, longitude]); // координаты пользователя
                  directions.setDestination([banks['latitude'], banks['longitude']]);
              });
          }

          else {
              console.log("Geolocation is not supported by this browser.");
          }
      });
  })
}