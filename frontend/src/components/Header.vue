<template>
  <q-header class="bg-primary text-white" height-hint="98">
    <q-toolbar>
      <q-toolbar-title>
        MS
      </q-toolbar-title>

      <q-btn dense flat round icon="menu" @click="toggleDrawer" />
    </q-toolbar>

    <q-tabs align="center">
      <q-route-tab to="/page1" label="Page One" />
      <q-route-tab to="/page2" label="Page Two" />
      <q-route-tab to="/page3" label="Page Three" />
    </q-tabs>
  </q-header>

  <Sidebar :rightDrawerOpen="rightDrawerOpen" />
</template>

<script lang="ts" setup>
import Sidebar from './Sidebar.vue';

const rightDrawerOpen = useState<boolean>(() => false);

const toggleDrawer = () => {
  rightDrawerOpen.value = !rightDrawerOpen.value;
}
</script>

<style>
</style>