<template>
    <div class="column q-mt-md">
        <p class="text-h6">Na sam koniec powiedz gdzie to się stało</p>
        <q-btn v-if="cordsDone" @click="useLocation()">Znajdź mnie</q-btn>
        <q-btn v-else icon="check" color="positive" disable class="undisable-btn">Dziękujemy</q-btn>
    </div>
</template>

<script lang="ts" setup>
import { useEventStore } from '@/stores/event'
const eventStore = useEventStore()
const cordsDone = useState<boolean>(() => false)

const useLocation = () => {
    const success =  (position: any) => {
        eventStore.latitiude = position.coords.latitude;
        eventStore.longitude = position.coords.longitude;
        cordsDone.value = true
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