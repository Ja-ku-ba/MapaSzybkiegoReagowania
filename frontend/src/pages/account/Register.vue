<template>
    <div class="q-pa-md" style="max-width: 400px">
        <q-form
            @submit="onSubmit"
            class="q-gutter-md fixed-center"
        >
            <q-input
                label="Nazwa użytkownika"
                filled
                v-model="username"
                type="text"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'To pole jest wymagane']"
            />
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

            <div class="flex items-center">
                <q-checkbox v-model="termsRules" label="Zgadzaam się z polityką prywatności serwisu&nbsp" />
                <NuxtLink class="policy" href='https://en.wikipedia.org/wiki/Special:Random'>Jakiś link</NuxtLink>
            </div>
            
            <div class="flex">
                <q-btn label="Zarejestruj" class="q-mx-auto" type="submit" color="primary"/>
            </div>

            <div class="column">
                <p class="q-mx-auto q-ma-none">Masz już konto?</p>
                <NuxtLink class="q-mx-auto policy" to="/account/login">Zaloguj się</NuxtLink>
            </div>
        </q-form>
    </div>
</template>

<script setup lang="ts">
const { $axios, $q } = useNuxtApp();
import { useUserStore } from '@/stores/user';
const userStore = useUserStore();

const email = useState<string>(() => '')
const username = useState<string>(() => '')
const password = useState<string>(() => '')
const showPassword = useState<Boolean>(() => false)
const termsRules = useState<Boolean>(() => false)

const onSubmit = async () => {
    if (termsRules.value !== true) {
        $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            position: 'top',
            message: 'Musisz wyrazić zgodę, aby założyć konto'
        })
    } else if (email.value === '' || password.value == '') {
        $q.notify({
            color: 'red-5',
            textColor: 'white',
            icon: 'warning',
            position: 'top',
            message: 'Musisz podać adres email i hasło aby kontynuować'
        })
    } else {
        
        await $axios.post('account/register/', {
            email: email.value,
            password: password.value,
            username: username.value
        }).then((response) => {
            console.log(response)
            $q.notify({
                color: 'green-4',
                textColor: 'white',
                icon: 'cloud_done',
                position: 'top',
                message: 'Konto zostało założne'
            })
            userStore.login(email.value, password.value)

        }).catch((error) => {
            let message = 'Wystąpił błąd podczas przetwarzania żądania.';

            const errorData = JSON.parse(error.request?.response || '{}');
            console.log("Odpowiedź serwera:", errorData);
            
            if (typeof errorData === 'object' && errorData !== null) {
                const errorMessages = Object.values(errorData)
                    .flat()
                    .join('<br >');
                message = errorMessages || message;
            }

            $q.notify({
                color: 'red',
                position: 'top',
                textColor: 'white',
                icon: 'error',
                message: message,
                html: true 
            });
        });
     }
}
</script>

<style scoped>
.policy {
    text-decoration: underline;
}
</style>