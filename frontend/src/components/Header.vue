<template>
  <q-header class="bg-primary text-white" height-hint="98">
    <q-toolbar>
      <q-toolbar-title>
        <NuxtLink to="/" class="text-white">
          MSR - mapa szybkiego reagowania
        </NuxtLink>
      </q-toolbar-title>
      
      <q-btn dense flat round icon="menu" @click="toggleDrawer" />
    </q-toolbar>

    <q-tabs align="center">
      <q-route-tab to="/map/natural" label="Naturalne" />
      <q-route-tab to="/map/law" label="Porządkowe" />
      <q-route-tab to="/map/utilities" label="Komunalne" />
    </q-tabs>
  </q-header>
</template>

<script lang="ts" setup>

const rightDrawerOpen = useState('rightDrawerOpen', () => false);
const toggleDrawer = () => {
  rightDrawerOpen.value = !rightDrawerOpen.value;
};
</script>

<style>
</style>
