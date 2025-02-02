<template>
  <div class="home-container">
    <div class="row">
      <div class="col-xs-12 col-sm-12 col-md-10 col-lg-8 q-mx-auto">
        <q-form @submit="onSubmit" class="q-pa-md box">
            <div class="full-width">
                <h1 class="text-h5 text-center">Zobacz co się dzieje w Twojej okolicy</h1>
                <q-input v-model="search" rounded outlined label="Skąd jesteś?" type="search" class="w-100">
                    <template v-slot:append>
                        <q-icon name="search" />
                    </template>
                </q-input>
            </div>
        </q-form>
    </div>

      <div class="col-xs-12 col-sm-12 col-md-10 col-lg-8 box q-mx-auto">
        <div class="column">
            <p class="text-h6 q-mx-auto">Lub sprawdź ostrzeżenia</p>
            <div class="row q-gutter-md justify-center">
            <NuxtLink to="map/all" class="column text-center">
                <q-icon name="public" size="48px" class="main-page-icon" />
                <span>Wszystkie</span>
            </NuxtLink>
            <NuxtLink to="map/natural" class="column text-center">
                <q-icon name="bolt" size="48px" class="main-page-icon" />
                <span>Naturalne</span>
            </NuxtLink>
            <NuxtLink to="map/law" class="column text-center">
                <q-icon name="local_police" size="48px" class="main-page-icon" />
                <span>Porządkowe</span>
            </NuxtLink>
            <NuxtLink to="map/utilities" class="column text-center">
                <q-icon name="delete_sweep" size="48px" class="main-page-icon" />
                <span>Komunalne</span>
            </NuxtLink>
            </div>
        </div>
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

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.box {
  border: 1px solid lime;
  height: 150px;
  display: flex;
  align-items: center;
  justify-content: center;
}

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
