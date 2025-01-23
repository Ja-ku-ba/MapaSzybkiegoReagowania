<template>
    <div class="row fixed-center w-100">
        <q-form @submit="onSubmit()" class="q-pb-lg col-md-12 col-lg-12">
            <h1 class="text-h5 q-mx-auto">Zobacz co się dzieje w Twojej okolicy</h1>
            <q-input v-model="search" rounded outlined label="Skąd jesteś?" type="search" style="width: 100%;">
                <template v-slot:append>
                    <q-icon name="search" />
                </template>
            </q-input>
        </q-form>
        <div class="q-mx-auto">
            <div class="flex flex-center">
                <p class="text-h6">Lub sprawdź ostrzeżenia</p>
            </div>
            <div class="row">
                <NuxtLink to="map/all" class="column q-mx-md">
                    <q-icon name="public" size="48px" class="q-mx-auto main-page-icon" />
                    <span>Wszystkie</span>
                </NuxtLink>
                <NuxtLink to="map/natural" class="column q-mx-md">
                    <q-icon name="bolt" size="48px" class="q-mx-auto main-page-icon" />
                    <span>Naturalne</span>
                </NuxtLink>
                <NuxtLink to="map/law" class="column q-mx-md">
                    <q-icon name="local_police" size="48px" class="q-mx-auto main-page-icon" />
                    <span>Porządkowe</span>
                </NuxtLink>
                <NuxtLink to="map/utilities" class="column q-mx-md">
                    <q-icon name="delete_sweep" size="48px" class="q-mx-auto main-page-icon" />
                    <span>Komunalne</span>
                </NuxtLink>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
const search = useState<string>(() => '')

const onSubmit = () => {
    console.log(12321)
}
</script>

<style>
.main-page-icon {
    border: 1px solid grey;
    padding: 10px;
    border-radius: 50px;
    color: grey;
}

.main-page-icon:hover {
    background: grey;
    color: white;
}
</style>