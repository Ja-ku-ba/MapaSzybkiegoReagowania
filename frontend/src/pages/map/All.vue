<template>
    <ClientOnly>
        <Map v-if="isPageLoaded" type="all"/>
    </ClientOnly>
</template>
    
<script setup lang="ts">
const isPageLoaded = useState<boolean>(() => false);
      
onMounted(async () => {
    isPageLoaded.value = true;
});
</script>
      