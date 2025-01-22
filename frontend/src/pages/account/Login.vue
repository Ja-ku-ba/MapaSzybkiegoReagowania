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
                hint="Adres email użyty podczas rejestracji"
                lazy-rules
                :rules="[
                    val => val && val.length > 0 || 'This field is required',
                    val => /.+@.+\..+/.test(val) || 'Please enter a valid email address'
                ]"
            />

            <q-input
                v-model="password"
                filled
                :type="showPassword ? 'text' : 'password'"
                label="Hasło"
                :rules="[
                    val => val && val.length >= 8 || 'Password must be at least 8 characters long'
                ]"
            >
                <template v-slot:append>
                    <q-icon
                        :name="showPassword ? 'visibility': 'visibility_off'"
                        class="cursor-pointer"
                        @click="showPassword = !showPassword"
                    />
                </template>
            </q-input>

            <div>
                <q-btn label="Zaloguj" class="q-mx-auto" type="submit" color="primary"/>
            </div>

            <div>
                <p>Nie masz jeszcze konta?</p>
                <NuxtLink to="/account/register">Zarejestruj się</NuxtLink>
            </div>
        </q-form>
    </div>
</template>

<script setup lang="ts">
import { useQuasar } from 'quasar'
import { useUserStore } from '~~/stores/user';

const userStore = useUserStore()
const $q = useQuasar()

const email = useState<string>(() => '')
const password = useState<string>(() => '')
const accept = useState<boolean>(() => false)
const showPassword = useState<boolean>(() => false)

const onSubmit = async () => {
    try {
        await userStore.login(email.value, password.value);
        $q.notify({
            textColor: 'white',
            icon: 'success',
            position: 'top',
            message: 'WItaj ponownie!'
        })
        await navigateTo('/')
    } catch (error) {
        $q.notify({
            color: 'warning',
            textColor: 'white',
            icon: 'cloud_done',
            position: 'top',
            message: 'Nie znaleziono konta o podanym adresie email lub hasło jest nieprawidłowe'
        })
    }
}

interface Profile {
    username: string;
    email: string;
}
</script>
