<template>
    <div class="home-container fixed-center">
      <div class="row">
        <div class="col-xs-11 col-sm-8 col-md-4 col-lg-3 q-mx-auto">
            <q-form @submit="onSubmit">
                <q-input label="Email" filled v-model="email" type="email" hint="Adres email użyty podczas rejestracji"
                    lazy-rules :rules="[
                        val => val && val.length > 0 || 'To pole jest wymagane',
                        val => /.+@.+\..+/.test(val) || 'Proszę, wprowadź poprawny adres email'
                    ]" />

                <q-input v-model="password" filled :type="showPassword ? 'text' : 'password'" label="Hasło" :rules="[
                    val => val && val.length >= 8 || 'Hasło musi mieć co najmniej 8 znaków'
                ]" class="q-mt-md">
                    <template v-slot:append>
                        <q-icon :name="showPassword ? 'visibility' : 'visibility_off'" class="cursor-pointer"
                            @click="showPassword = !showPassword" />
                    </template>
                </q-input>

                <div class="flex q-mt-md justify-center">
                    <q-btn class="col-sm-3" label="Zaloguj" type="submit" color="primary" />
                </div>

                <div class="column q-mt-lg">
                    <p class="q-mb-none text-center">Nie masz jeszcze konta?</p>
                    <NuxtLink class="normal-link text-center" to="/account/register">Zarejestruj się</NuxtLink>
                </div>
            </q-form>
        </div>
    </div>
    </div>
</template>

<script setup lang="ts">
import { useQuasar } from 'quasar';

const userStore = useUserStore();
const $q = useQuasar();

const email = useState<string>(() => '');
const password = useState<string>(() => '');
const showPassword = useState<boolean>(() => false);

definePageMeta({
  middleware: ['auth-guard']
})

const onSubmit = async () => {
    try {
        await userStore.login(email.value, password.value);
        $q.notify({
            textColor: 'white',
            icon: 'success',
            position: 'top',
            message: 'Witaj ponownie!'
        });
        await navigateTo('/');
    } catch (error) {
        $q.notify({
            color: 'negative',
            textColor: 'white',
            icon: 'error',
            position: 'top',
            message: 'Nie znaleziono konta o podanym adresie email lub hasło jest nieprawidłowe'
        });
    }
};
</script>
