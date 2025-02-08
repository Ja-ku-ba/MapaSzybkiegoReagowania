<template>
  <div style="height:100vh; width:100vw; margin-top: -98px;">
    <LMap ref="map" :zoom="13" :max-zoom="18" :minZoom="11" :center="[54.4672944, 17.0165414]"
      :use-global-leaflet="true" @ready="onMapReady">
      <LTileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&amp;copy; <a href=&quot;https://www.openstreetmap.org/&quot;>OpenStreetMap</a> contributors,  <a href='http://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='http://cloudmade.com'>CloudMade</a>"
        layer-type="base" name="OpenStreetMap" />
    </LMap>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
const { $axios } = useNuxtApp();
const map = ref<any>(null)
const locations = useState<ILocations>(() => [])

const locations2 = Array.from({ length: 352 }, (_, i) => ({
  name: `Marker ${i + 1}`,
  lat: 54.4672944 + (Math.random() - 0.5) * 0.08,
  lng: 17.0165414 + (Math.random() - 0.5) * 0.09,
}));
console.log(locations2)

const onMapReady = async () => {
  // let debounceTimer;
  // map.on('moveend', function() {
  //   clearTimeout(debounceTimer);
  //   debounceTimer = setTimeout(() => {
  //     // Wysyłanie zapytania
  //   }, 300); // Czekaj 300ms po zakończeniu ruchu mapy
  // });

  const mapBounds = map.value.leafletObject.getBounds();
  const sw = mapBounds.getSouthWest();
  const ne = mapBounds.getNorthEast();
  await getPoints(sw, ne)
  useLMarkerCluster({
    leafletObject: map.value.leafletObject,
    markers: locations.value
  });
  console.log(locations.value)
}

const props = defineProps(['type'])
const { params } = useRoute()
const getPoints = async (sw:any, ne:any) => {
  await $axios.get('event/map-markers/', {
    params: {
      sw: sw,
      ne: ne,
      type: props.type,
    }
  }).then((response: any) => {
    console.log(response)
    response.data.forEach((cords) => {
        locations.value.push({
          lat: cords.latitiude,
          lng: cords.longitude
       })
    })
  }).catch((error) => {
    console.log(error)
  })

  // $q.notify({
  //   color: 'warning',`
  //   textColor: 'white',
  //   icon: 'cloud_done',
  //   position: 'top',
  //   message: 'Zdarzenie dodane pomyślnie, zobaczysz je na mapie w ciągu 5 minut'
  // });

  return true
}

// const showBounds = () => {
//   if (!map.value || !map.value.leafletObject) {
//     console.error('Map is not ready yet!');
//     return;
//   }

//   const mapBounds = map.value.leafletObject.getBounds();
//   const sw = mapBounds.getSouthWest();
//   const ne = mapBounds.getNorthEast();

//   console.log('Bounds:', mapBounds);
//   console.log('South-West:', sw);
//   console.log('North-East:', ne);

//   console.log('SW lat:', sw.lat, 'SW lng:', sw.lng);
//   console.log('NE lat:', ne.lat, 'NE lng:', ne.lng);
// };
</script>
