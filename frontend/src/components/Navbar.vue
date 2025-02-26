<template>
    <nav class="bg-gray-800 text-white p-4 shadow-md w-full fixed top-0 left-0">
      <div class="container mx-auto flex justify-between items-center">
       
        <div class="flex items-center space-x-2">
          <LucideLayoutDashboard class="w-6 h-6 text-white" />
          <router-link to="/dashboard" class="text-xl font-semibold">Dashboard</router-link>
        </div>
        
       
        <div class="flex space-x-4">
          <router-link to="/users" class="nav-link">
            <LucideUsers class="w-5 h-5" />
            <span>Users</span>
          </router-link>
          <router-link to="/companies" class="nav-link">
            <LucideBuilding class="w-5 h-5" />
            <span>Companies</span>
          </router-link>
          <router-link to="/departments" class="nav-link">
            <LucideFolder class="w-5 h-5" />
            <span>Departments</span>
          </router-link>
          <router-link to="/employees" class="nav-link">
            <LucideUserCheck class="w-5 h-5" />
            <span>Employees</span>
          </router-link>
          
          <router-link to="/" class="nav-link">
            <LucideLogOut class="w-5 h-5" />
            <button @click="logout">Logout</button>
          </router-link>
        </div>
      </div>
    </nav>
  </template>

<script>
 import { LucideLayoutDashboard, LucideUsers, LucideBuilding, LucideFolder, LucideUserCheck, LucideLogOut } from 'lucide-vue-next';

export default {
    components: {
    LucideLayoutDashboard,
    LucideUsers,
    LucideBuilding,
    LucideFolder,
    LucideUserCheck,
    LucideLogOut
  },
    name: 'TheNavbar', 
    methods: {
        logout() {
            this.$store.dispatch('logout');
            this.$router.push('/');
        },
    },
};
</script>

<style>
.nav-link {  
  display: flex;  
  align-items: center;  
  gap: 0.5rem; 
  color: #D1D5DB; 
  transition: color 0.2s ease;  
}  

.nav-link:hover {  
  color: white;   
}
</style>
