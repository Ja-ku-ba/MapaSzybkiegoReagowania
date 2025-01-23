<template>
    <div class="colums q-mt-md">
        <span>Powiedz nam co się stało</span>
        <textarea v-model="description" @click="doAssigments()" class="full-width q-my-sm" rows="5" placeholder="Opisz zdarzenie"></textarea>
        <span>Czy chcesz aby inni widzieli ten opis?</span>
        <q-btn-toggle
            v-model="showUserDescription"
            @click="doAssigments()"
            spread
            toggle-color="primary"
            color="white"
            text-color="black"
            toggle-text-color="white"
            :options="[
                {label: 'Nie', value: false},
                {label: 'Tak', value: true}
            ]"
        />
    </div>
</template>

<script setup lang="ts">
import { useEventStore } from '@/stores/event'

const evnetStore = useEventStore()

const showUserDescription = useState<boolean>('showUserDescription', () => false)
const description = useState<string>(() => '')

const doAssigments = () => {
    eventStore.description = description.value
    eventStore.showDescription = showUserDescription.value
}
</script>
