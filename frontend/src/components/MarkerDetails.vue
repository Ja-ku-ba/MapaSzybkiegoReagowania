<template>
    <q-card>
      <q-card-section>
        <div class="text-h6">Doane: {{ formattedDate }}</div>
        <div class="text-subtitle2">Przez: {{ props.creator }}</div>
      </q-card-section>

      <q-card-section v-if="!!props.description" class="q-pt-none">
        {{ props.description }}
      </q-card-section>
    </q-card>
</template>

<script setup lang="ts">
import { QCard, QCardSection } from 'quasar';

const props = defineProps({
    creator: String,
    description: String,
    createdAt: String
});

const formattedDate = computed(() => {
  return props.createdAt ? new Date(props.createdAt).toLocaleDateString() : "Brak daty";
});
</script>
