<template>
    <div class="fixed-center">
        <div class="row">
            <div class="col-xs-11 col-sm-8 col-md-4 col-lg-3 q-mx-auto">
                <q-form @submit="onSubmit()">
                    <q-input label="Nazwa użytkownika" filled v-model="username" type="text" lazy-rules
                        :rules="[val => val && val.length > 0 || 'To pole jest wymagane']" />
                    <q-input label="Email" filled v-model="email" type="email" lazy-rules
                        :rules="[val => val && val.length > 0 || 'To pole jest wymagane']" />

                    <q-input v-model="password" filled :type="showPassword ? 'text' : 'password'" label="Hasło">
                        <template v-slot:append>
                            <q-icon :name="showPassword ? 'visibility' : 'visibility_off'" class="cursor-pointer"
                                @click="showPassword = !showPassword" />
                        </template>
                    </q-input>

                    <div class="q-mt-md">
                        <q-checkbox v-model="termsRules" label="Zgadzaam się z polityką prywatności serwisu, ">
                            <NuxtLink class="normal-link" href='https://en.wikipedia.org/wiki/Special:Random' target="_blank">
                                poityka serwisu
                            </NuxtLink>
                        </q-checkbox>
                    </div>

                    <div class="flex q-mt-lg">
                        <q-btn label="Zarejestruj" class="q-mx-auto" type="submit" color="primary" />
                    </div>

                    <div class="column q-mt-lg">
                        <p class="q-mx-auto q-mb-none q-mt-sm">Masz już konto?</p>
                        <NuxtLink class="q-mx-auto normal-link" to="/account/login">Zaloguj się</NuxtLink>
                    </div>
                </q-form>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
const { $axios, $q } = useNuxtApp();
const userStore = useUserStore();

const email = useState<string>(() => '')
const username = useState<string>(() => '')
const password = useState<string>(() => '')
const showPassword = useState<Boolean>(() => false)
const termsRules = useState<Boolean>(() => false)

definePageMeta({
  middleware: ['auth-guard']
})

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
