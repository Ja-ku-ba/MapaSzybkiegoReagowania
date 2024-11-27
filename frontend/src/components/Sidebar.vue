<template>
  <q-drawer v-if="rightDrawerOpen" side="right" overlay behavior="mobile">
    <!-- drawer content -->
  </q-drawer>
</template>

<script setup lang="ts">
const props = defineProps<{
  rightDrawerOpen: boolean
}>()
// const props = defineProps(['rightDrawerOpen'])
</script>