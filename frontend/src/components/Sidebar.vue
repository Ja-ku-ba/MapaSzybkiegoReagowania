<template>
  <q-drawer
    side="right"
    v-if="rightDrawerOpen"
    bordered
    :width="300"
    show-if-above
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
const rightDrawerOpen = useState('rightDrawerOpen');
</script>

<style scoped>
</style>