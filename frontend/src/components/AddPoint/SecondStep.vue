<template>
    <div class="col-xs-12 col-sm-4 col-md-10 col-lg-10 q-gutter-md q-mt-md">
        <p class="text-h6">Powiedz nam co się stało</p>
        <q-input type="textarea" v-model="description" @update:model-value="doAssigments()" class="q-my-sm" rows="5" placeholder="Opisz zdarzenie"></q-input>
        <span>Czy chcesz aby inni widzieli ten opis?</span>
        <q-btn-toggle
            v-model="showUserDescription"
            @click="doAssigments()"
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
import { useEventStore } from '@/stores/event'

const eventStore = useEventStore()

const showUserDescription = useState<boolean>('showUserDescription', () => false)
const description = useState<string>('description', () => '')

const doAssigments = () => {
    eventStore.description = description.value
    eventStore.showDescription = showUserDescription.value
}
</script>
