<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated>
      <Header />
    </q-header>

    <q-page-container>
      <NuxtLayout>
        <NuxtPage />
      </NuxtLayout>
    </q-page-container>

    <!-- <q-footer>
      <div class="text-center">Footer Content</div>
    </q-footer> -->
  </q-layout>
</template>

<script setup lang="ts">
  import Header from './src/components/Header.vue'; 
</script>

<style scoped>
  /* Style dla aplikacji */
</style>
