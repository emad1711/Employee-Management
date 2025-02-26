<template>
    <div class="p-10 overflow-x-auto mt-6 w-full">
      <h2 class="text-3xl font-semibold text-gray-800 flex items-center">
        <LucideHome class="w-7 h-7 text-blue-600 mr-2" />
        Dashboard
      </h2>
      <p class="text-lg text-gray-600 mt-4">
        Welcome, <span class="font-bold text-blue-600">{{userEmail }}</span>!
      </p>
    </div>
  </template>
  
  <script>
  import { mapState } from "vuex";
  import { LucideHome } from 'lucide-vue-next';
  
  export default {
    name: "TheDashboard",
    components: { LucideHome },
    computed: {
      ...mapState({
        userEmail: state => state.user.username
      })
    }
  };
  </script>
 