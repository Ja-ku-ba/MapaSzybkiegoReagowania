<template>
  <q-drawer 
    ref="drawerRef" 
    side="right" 
    v-model="rightDrawerOpen" 
    bordered 
  >
    <q-scroll-area class="fit q-pa-lg column">
      <div v-if="userStore.isAuthenticated">
        <span>@{{userStore.user.username}}</span>
        <q-separator />
        <NuxtLink @click="userStore.logout()">Wyloguj</NuxtLink>
      </div>  
      <div v-else class="q-pa-md">
        <NuxtLink to="account/login">Zaloguj</NuxtLink>
      </div>
    </q-scroll-area>
  </q-drawer>
</template>

<script setup lang="ts">
import { useUserStore } from '~~/stores/user';

const userStore = useUserStore()
const rightDrawerOpen = useState<boolean>('rightDrawerOpen');
</script>

<style scoped>
</style>
