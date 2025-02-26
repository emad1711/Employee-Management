<template>
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
      <div class="bg-white p-8 shadow-lg rounded-lg w-96">
        <h2 class="text-2xl font-semibold text-gray-700 text-center mb-6">Login</h2>
        <form @submit.prevent="login" class="space-y-4">
          <div class="flex items-center border border-gray-300 rounded-lg px-3 py-2">
            <LucideMail class="w-5 h-5 text-gray-500" />
            <input 
              type="email" 
              v-model="email" 
              placeholder="Email" 
              required 
              class="w-full outline-none pl-3"
            />
          </div>
          <div class="flex items-center border border-gray-300 rounded-lg px-3 py-2">
            <LucideLock class="w-5 h-5 text-gray-500" />
            <input 
              type="password" 
              v-model="password" 
              placeholder="Password" 
              required 
              class="w-full outline-none pl-3"
            />
          </div>
          <button 
            type="submit" 
            class="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition"
          >
            Login
          </button>
        </form>
        <p v-if="error" class="text-red-500 text-sm text-center mt-3">{{ error }}</p>
      </div>
    </div>
  </template>

<script>
import { LucideMail, LucideLock } from 'lucide-vue-next';
import { mapGetters } from 'vuex'; 

export default {
    components: {
    LucideMail,
    LucideLock,
  },
    name: 'TheLogin', 
    data() {
        return {
            email: '',
            password: '',
            error: '',
        };
    },
    computed: {  
      ...mapGetters(['currentUser'])
    },  
    methods: {
        async login() {
            try {
                await this.$store.dispatch('login', {
                    email: this.email,
                    password: this.password,
                });
                this.$router.push('/dashboard');
            } catch (error) {
                this.error = 'Login failed. Please check your credentials.';
            }
        },
    },
};
</script>