<template>
  <!-- {{ error }} -->
    <div class="error-page">
        <div v-if="error.statusCode === 404">
            <h1>404 - Strona nie została znaleziona</h1>
            <q-btn to="/">Strona główna</q-btn>
        </div>
        <h1 v-else>Coś poszło nie tak, spróbuj ponownie za chwilę.</h1>
    </div>
  </template>
  
<script setup lang="ts">
defineProps<{ error: { statusCode: number; message: string } }>()
</script>

<style scoped>
  .error-page {
    text-align: center;
    padding: 50px;
  }
</style>
