<template>
    <div class="columm q-mt-md">
        <span>Na sam koniec powiedz gdzie to się stało</span>
        <q-btn @click="useLocation()">Znajdź mnie</q-btn>
    </div>
</template>

<script lang="ts" setup>
import { useEventStore } from '@/stores/event'
const eventStore = useEventStore()

const useLocation = () => {
    const success =  (position: any) => {
        eventStore.latitiude = position.coords.latitude;
        eventStore.longitude = position.coords.longitude;
    }

    const error = () => {
        console.log("Unable to retrieve your location");
    }

    if (!navigator.geolocation) {
        console.log("Unable to retrieve your location in this browser")
    } else {
        navigator.geolocation.getCurrentPosition(success, error);
    }
}
</script>
