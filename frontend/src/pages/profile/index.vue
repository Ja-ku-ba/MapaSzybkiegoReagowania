<template>
    <div class="q-pa-md column">
        <div class="row justify-center q-mb-sm">
            <q-card flat bordered class="col-12 col-sm-10 col-md-6 q-mx-auto"
                :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
                <q-card-section>
                    <div class="row items-center no-wrap">
                        <div class="col">
                            <div class="text-h6">Witaj, @{{ eventsList.username }}</div>
                            <div class="text-subtitle2">
                                Twój login: {{ eventsList.email }}
                            </div>
                            <div class="text-subtitle2">
                                Jesteś z nami od: {{ getNormalDate(eventsList.date_joined) }}
                            </div>
                        </div>
                    </div>
                </q-card-section>
            </q-card>
        </div>

        <div class="row justify-center">
            <div class="col-12 col-sm-10 col-md-6 col-lg-4">
                <q-list v-if="eventsList.events" bordered padding>
                    <q-item v-ripple v-for="(event, idx) in eventsList.events" :key="idx">
                        <q-item-section>
                            <q-item-label>Dodane: {{ getNormalDate(event.created_at) }}</q-item-label>
                            <q-item-label>Czy inni widzą opis: {{ event.show_description === true ? "Widzą" : "Nie widzą" }}</q-item-label>
                            <q-item-label caption>
                                Opis: {{ event.description }}
                            </q-item-label>
                        </q-item-section>
                    </q-item>
                </q-list>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import type { IUserEvents } from '~/types/userEvents'

const { $axios } = useNuxtApp()
const eventsList = useState<IUserEvents>(() => <IUserEvents>{})

definePageMeta({
  middleware: ['auth-guard']
})

onMounted(() => {
    getUserProfileInfo()
})

const getUserProfileInfo = async () => {
    try {
        const response = await $axios.get('account/profile/')
        eventsList.value = response.data
    } catch (error) {
        console.error('Error fetching user profile info:', error)
    }
}

const getNormalDate = (date: string) => {
    return new Date(date).toLocaleDateString()
}
</script>
