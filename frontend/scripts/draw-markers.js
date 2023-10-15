function DrawMarkers(http_link) {
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
  getData(http_link).then(banks => {
      var geojson = {
          type: 'FeatureCollection',
          features: []
      };
      banks.forEach(function (data) {
          var feature = {
              type: 'Feature',
              geometry: {
                  type: 'Point',
                  coordinates: [data.longitude, data.latitude]
              },
              properties: {
                  id: data.id,
                  title: data.title,
                  address: data.address,
                  photo: data.photo,
                  start_time: data.start_time,
                  end_time: data.end_time,
                  withdraw_rubles: data.withdraw_rubles,
                  put_rubles: data.put_rubles,
                  nfc: data.nfc,
                  withdraw_qr: data.withdraw_qr,
                  qr_payment: data.qr_payment,
                  for_visually_impaired: data.for_visually_impaired,
                  for_lm: data.for_lm,
                  workload: data.workload,
                  type: data.type
              }
          };
          geojson.features.push(feature);
      })

      map.on('load', () => {
          map.addSource('banks', {
              'type': 'geojson',
              'data': {
                  'type': 'FeatureCollection',
                  'features': geojson
              }
          });

          geojson['features'].forEach((element) => {
              const marker1 = new mapboxgl.Marker()
                  .setLngLat(element['geometry']['coordinates'])
                  .addTo(map);
          });
      });
  })
}