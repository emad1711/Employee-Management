<template>
  <div id="app" class="h-screen flex flex-col">
    <TheNavbar v-if="$store.getters.isAuthenticated" />
    <div class="flex-1">
      <router-view />
    </div>
  </div>
</template>

<script>
import TheNavbar from '@/components/Navbar.vue';

export default {
  components: {
    TheNavbar,
  },
};
</script>

