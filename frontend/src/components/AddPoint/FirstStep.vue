<template>
    <div class="col-xs-12 col-sm-4 col-md-10 col-lg-10 q-gutter-md q-mt-md">
        <p class="text-h6">Wybierz kategorię</p>
        <q-btn class="full-width q-my-sm" @click="assignType('nat')">
            <q-icon name="bolt" size="48px" class="q-mr-sm select-event-icon" />
            <span>Naturalne</span>
        </q-btn>

        <q-btn class="full-width q-my-sm" @click="assignType('law')">
            <q-icon name="local_police" size="48px" class="q-mr-sm select-event-icon" />
            <span>Porządkowe</span>
        </q-btn>

        <q-btn class="full-width q-my-sm" @click="assignType('utl')">
            <q-icon name="delete_sweep" size="48px" class="q-mr-sm select-event-icon" />
            <span>Komunalne</span>
        </q-btn>
    </div>
</template>

<script setup lang="ts">
import { useEventStore } from '~/stores/event';
const emits = defineEmits(['nextStep'])
const eventStore = useEventStore()

const assignType = (type: string) => {
    eventStore.type = type,
    emits('nextStep')
}
</script>

<style lang="scss" scoped>
.q-btn ::deep(.q-btn_content) {
  justify-content: start;
}

.select-event-icon {
    border: 1px solid grey;
    padding: 10px;
    border-radius: 50px;
    color: grey;
}
</style>