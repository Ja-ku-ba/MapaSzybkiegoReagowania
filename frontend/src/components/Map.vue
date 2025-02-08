<template>
  <div style="height:100vh; width:100vw; margin-top: -98px;">
    <LMap ref="map" :zoom="12" :max-zoom="18" :minZoom="11" :center="[54.4672944, 17.0165414]"
      :use-global-leaflet="true" @ready="onMapReady">
      <LTileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&amp;copy; <a href=&quot;https://www.openstreetmap.org/&quot;>OpenStreetMap</a> contributors,  <a href='http://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='http://cloudmade.com'>CloudMade</a>"
        layer-type="base" name="OpenStreetMap" />
    </LMap>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import type { ILocation } from '~/types/location';
import type { ILocations } from '~/types/locations';
const { $axios } = useNuxtApp();
const map = ref<any>(null)
const locations = useState<ILocations>(() => [])
const props = defineProps(['type'])

const onMapReady = async () => {
  locations.value = []

  const mapBounds = map.value.leafletObject.getBounds();
  const sw = mapBounds.getSouthWest();
  const ne = mapBounds.getNorthEast();
  const points = await getPoints(sw, ne);

  let debounceTimer: NodeJS.Timeout;
  map.value.leafletObject.on('moveend', function() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(async () => {
      const mapBounds = map.value.leafletObject.getBounds();
      const sw = mapBounds.getSouthWest();
      const ne = mapBounds.getNorthEast();
      const points = await getPoints(sw, ne);
      genereateMarkers(transformPoints(points));
    }, 300);
  });
  
  genereateMarkers(transformPoints(points));
}

const genereateMarkers = (newPoints: ILocations) => {
  console.log(newPoints)
  useLMarkerCluster({
    leafletObject: map.value.leafletObject,
    markers: newPoints
  });
}

const getPoints = async (sw: any, ne: any): Promise<ILocations> => {
  try {
    const response = await $axios.get('event/map-markers/', {
      params: {
        swLat: sw.lat,
        swLong: sw.lng,
        neLat: ne.lat,
        neLong: ne.lng,
        type: props.type,
      }
    });

    console.log(response);
    
    return response.data;
  } catch (error) {
    console.error('Error fetching points:', error);
    return [];
  }
}

const transformPoints = (points: ILocations):ILocations => {
  let pointsList:ILocations = []
  points.forEach((cords:ILocation) => {
    pointsList.push({
      lat: cords.latitiude,
      lng: cords.longitude
    })
  })
  return pointsList
}
</script>
