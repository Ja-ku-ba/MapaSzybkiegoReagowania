<template>
  <q-drawer ref="drawerRef" side="right" v-model="rightDrawerOpen" bordered overlay>
    <q-scroll-area class="fit">
      <q-list>
        <div v-if="userStore.isAuthenticated">
        <template v-for="(menuItem, index) in menuList" :key="index">
          <q-item clickable v-ripple :to='`/${menuItem.route}`'>
            <q-item-section avatar class="q-pr-none">
              <q-icon :name="menuItem.icon" class="q-pr-none" />
            </q-item-section>
            <q-item-section>
              @{{ menuItem.label }}
            </q-item-section>
          </q-item>
          <q-separator />
        </template>
          <q-item clickable v-ripple @click="userStore.logout()">
            <q-item-section avatar class="q-pr-none">
              <q-icon name="logout" class="q-pr-none" />
            </q-item-section>
            <q-item-section>
              Wyloguj
            </q-item-section>
          </q-item>
        </div>
        <div v-else>
          <q-item clickable v-ripple to="/account/login">
            <q-item-section avatar class="q-pr-none">
              <q-icon name="login" class="q-pr-none" />
            </q-item-section>
            <q-item-section>
              Zaloguj
            </q-item-section>
          </q-item>
        </div>
      </q-list>
    </q-scroll-area>
  </q-drawer>
</template>

<script setup lang="ts">
const userStore = useUserStore()
const rightDrawerOpen = useState<boolean>('rightDrawerOpen');

const menuList = useState(() =>
  [{
    icon: 'person',
    label: userStore.isAuthenticated ? userStore.user.username : 'Gość',
    route: 'profile'
  }]
) 
</script>

<style scoped></style>
