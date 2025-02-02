<template>
    <div class="col-xs-12 col-sm-4 col-md-10 col-lg-10 q-gutter-md q-mt-md">
        <q-btn class="full-width q-my-sm" @click="$emit('setStep', 1)">
        <q-icon name="public" size="48px" class="q-mr-sm select-event-icon" />
        <span>Wszystkie</span>
        </q-btn>
        <q-btn class="full-width q-my-sm" @click="$emit('setStep', 1)">
        <q-icon name="bolt" size="48px" class="q-mr-sm select-event-icon" />
        <span>Naturalne</span>
        </q-btn>

        <q-btn class="full-width q-my-sm" @click="$emit('setStep', 1)">
        <q-icon name="local_police" size="48px" class="q-mr-sm select-event-icon" />
        <span>Porządkowe</span>
        </q-btn>

        <q-btn class="full-width q-my-sm" @click="$emit('setStep', 1)">
        <q-icon name="delete_sweep" size="48px" class="q-mr-sm select-event-icon" />
        <span>Komunalne</span>
        </q-btn>
    </div>
</template>

<script setup lang="ts">
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