<template>
    <div class="column q-mt-md">
        <p class="text-h6">Na sam koniec powiedz gdzie to się stało</p>
        {{ showFindMe }} - {{ !eventStore.validState }}
        <q-btn v-if="showFindMe()" @click="useLocation()">Znajdź mnie</q-btn>
        <q-btn v-else icon="check" color="positive" disable class="undisable-btn">Dziękujemy</q-btn>
    </div>
</template>

<script lang="ts" setup>
import { useEventStore } from '@/stores/event'
const eventStore = useEventStore()

const showFindMe = () => {
    return !eventStore.latitiude && !eventStore.longitude && !eventStore.validState()
}

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

<style>
.undisable-btn {
    opacity: 1 !important;
}
</style>