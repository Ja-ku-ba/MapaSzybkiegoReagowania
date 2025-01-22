<template>
  <q-layout view="hHh lpR fFf">
    <q-page-container>
      <NuxtLayout>
        <Header />
        <NuxtPage />
        <div v-if="userStore.isAuthenticated">
          <AddPoint />
        </div>
        <Sidebar />
        <Footer />
      </NuxtLayout>
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)


import { useUserStore } from '@/stores/user';
const userStore = useUserStore();
userStore.initializeUser();

</script>

<style>
a {
    all: unset;
    cursor: pointer;
}
</style>
