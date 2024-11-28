<template>
  <q-drawer
    side="right"
    v-if="rightDrawerOpen"
    bordered
    :width="300"
    show-if-above
  >
    <q-scroll-area class="fit">
      <div class="q-pa-sm">
        <div v-for="n in 50" :key="n">Drawer {{ n }} / 50</div>
      </div>
    </q-scroll-area>
  </q-drawer>
</template>

<script setup lang="ts">
const props = defineProps(['rightDrawerOpen']);
</script>

<style scoped>
</style>