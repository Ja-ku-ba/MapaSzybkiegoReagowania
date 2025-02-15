<template>
    <div class="col-xs-12 col-sm-4 col-md-10 col-lg-10 q-gutter-md q-mt-md">
        <p class="text-h6">Powiedz nam co się stało</p>
        <q-input 
            type="textarea"
            v-model="eventStore.description"
            class="q-my-sm"
            rows="5"
            placeholder="Opisz zdarzenie"
            :rules="[ val => val.length <= 1000 || 'Limit to 1000 znaków']"    
        ></q-input>
        <span>Czy chcesz aby inni widzieli ten opis?</span>
        <q-btn-toggle
            v-model="eventStore.showDescription"
            spread
            toggle-color="white"
            toggle-text-color="black"
            color="primary"
            text-color="white"
            :options="[
                {label: 'Nie', value: false},
                {label: 'Tak', value: true}
            ]"
        />
    </div>
</template>

<script setup lang="ts">
// import { useEventStore } from '@/stores/event'

const eventStore = useEventStore()
</script>
