<template>
  <q-layout view="hHh lpR fFf">
    <q-page-container>
      <NuxtLayout>
        <Header />
        <client-only>
          <q-linear-progress
            v-if="isLoading"
            :key="isLoading"
            class="page-loader"
            :animation-speed="500"
            stripe
            rounded
            color="negative"
            :value="loading.progress"
            indeterminate
          />
        </client-only>
        <NuxtPage id="index" />
        
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
import { computed } from 'vue';
import { useUserStore } from '@/stores/user';
const userStore = useUserStore();

const loading = useNuxtApp().$loading;
const isLoading = computed(() => loading.isLoading.value);

onBeforeMount(() => {
  loading.start();
});

onMounted(() => {
  loading.stop();
});
</script>

<style>
a {
    all: unset;
    cursor: pointer;
}

.normal-link {
    color: #1976D2;
    text-decoration: none;
}

.normal-link:hover {
    text-decoration: underline;
}
</style>

<style scoped>
#index {
  width: 100vw;
  /* height: calc(100vh - 98px - 21px); */
}

.page-loader {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  z-index: 9999;
  height: 6px;
}
</style>
