<template>
  <div style="height:100vh; width:100vw; margin-top: -98px;">
    <LMap ref="map" :zoom="12" :max-zoom="18" :minZoom="11" :center="getCenterCords()"
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
import { createApp } from 'vue';
const { $axios } = useNuxtApp();
const map = ref<any>(null)
const locations = useState<ILocations>(() => [])
const props = defineProps(['type'])
const mapCords = useState<any>('mapCords')

const onMapReady = async () => {
  if (!map.value || !map.value.leafletObject) return;

  const leafletMap = map.value.leafletObject;
  leafletMap.addLayer(markerClusterGroup);

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

import MarkerDetails from "../components/MarkerDetails.vue";
import L from 'leaflet';
import 'leaflet.markercluster';
import { Quasar } from "quasar";
const markerClusterGroup = L.markerClusterGroup();
const genereateMarkers = (newPoints: ILocations) => {
  markerClusterGroup.clearLayers();

  newPoints.forEach(point => {
  const marker = L.marker([point.lat, point.lng]);

  const popupContainer = document.createElement('div');
  const app = createApp(MarkerDetails, { 
    creator: point.creator, 
    description: point.description, 
    createdAt: point.created_at 
  });
  app.use(Quasar);
  app.mount(popupContainer);
  marker.bindPopup(popupContainer);
  markerClusterGroup.addLayer(marker);
});


  map.value.leafletObject.addLayer(markerClusterGroup);
};

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

const getCenterCords = () => {
  let center = []
  if (!!mapCords.value && mapCords.value.length > 0) {
    center = mapCords.value
  } else {
    center = [54.4672944, 17.0165414]
  }
  return center
}
</script>
