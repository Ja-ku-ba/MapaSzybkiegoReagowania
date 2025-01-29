<template>
    <div class="colums q-mt-md">
        <span>Powiedz nam co się stało</span>
        <q-input type="textarea" v-model="description" @update:model-value="doAssigments()" class="full-width q-my-sm" rows="5" placeholder="Opisz zdarzenie"></q-input>
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

const eventStore = useEventStore()

const showUserDescription = useState<boolean>('showUserDescription', () => false)
const description = useState<string>('description', () => '')

const doAssigments = () => {
    eventStore.description = description.value
    eventStore.showDescription = showUserDescription.value
}
</script>
