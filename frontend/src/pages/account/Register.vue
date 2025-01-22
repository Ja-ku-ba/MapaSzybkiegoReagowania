<template>
    <div class="q-pa-md" style="max-width: 400px">
        <q-form
            @submit="onSubmit"
            class="q-gutter-md fixed-center"
        >
            <q-input
                label="Email"
                filled
                v-model="email"
                type="email"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'To pole jest wymagane']"
            />

            <q-input v-model="password" filled :type="showPassword ? 'text':'password'" label="Hasło">
                <template v-slot:append>
                    <q-icon
                        :name="showPassword ? 'visibility': 'visibility_off'"
                        class="cursor-pointer"
                        @click="showPassword = !showPassword"
                    />
                </template>
            </q-input>

            <div>
                <q-checkbox v-model="termsRules" label="Zgadzaam się z polityką prywatności serwisu" />
                <NuxtLink class="policy" href='https://en.wikipedia.org/wiki/Special:Random'>Jakiś link</NuxtLink>
            </div>
            
            <div>
                <q-btn label="Zarejestruj" class="q-mx-auto" type="submit" color="primary"/>
            </div>

            <div>
                <p>Masz już konto?</p>
                <NuxtLink to="/account/login">Zaloguj się</NuxtLink>
            </div>
        </q-form>
    </div>
</template>

<script setup lang="ts">
import { useQuasar } from 'quasar'

const $q = useQuasar()

const email = useState<string>(() => '')
const password = useState<string>(() => '')
const accept = useState<Boolean>(() => false)
const showPassword = useState<Boolean>(() => false)
const termsRules = useState<Boolean>(() => false)

const onSubmit = () => {
    if (accept.value !== true) {
        $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            message: 'You need to accept the license and terms first'
        })
    }
    else {
        $q.notify({
            color: 'green-4',
            textColor: 'white',
            icon: 'cloud_done',
            message: 'Submitted'
        })
    }
}
</script>

<style scoped>
.policy {
    text-decoration: underline;
}
</style>