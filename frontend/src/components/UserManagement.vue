<template>
    <div class="p-10 overflow-x-auto mt-6 w-full "> 
      <h2 class="text-2xl font-semibold text-gray-800 mb-4 flex items-center">
        <LucideUsers class="w-6 h-6 mr-2" /> User Management
      </h2>
  
     
      <button 
        @click="showCreateUserModal = true"
        class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition flex items-center"
      >
        <LucideUserPlus class="w-5 h-5 mr-2" /> Create User
      </button>
  
      
      <div class="overflow-x-auto mt-6">
        <table class="min-w-full w-full bg-white shadow-md rounded-lg">
          <thead>
            <tr class="bg-gray-800 text-white">
              <th class="py-3 px-4 text-left">ID</th>
              <th class="py-3 px-4 text-left">User Name</th>
              <th class="py-3 px-4 text-left">Email</th>
              <th class="py-3 px-4 text-left">Role</th>
              <th class="py-3 px-4 text-center">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in users" :key="user.id" class="border-b hover:bg-gray-100 transition">
              <td class="py-3 px-4">{{ user.id }}</td>
              <td class="py-3 px-4">{{ user.username }}</td>
              <td class="py-3 px-4">{{ user.email }}</td>
              <td class="py-3 px-4 capitalize">{{ user.role }}</td>
              <td class="py-3 px-4 text-center flex justify-center space-x-4">
                <button 
                  @click="openEditModal(user)" 
                  class="bg-yellow-500 text-white px-3 py-1 rounded-md hover:bg-yellow-600 transition flex items-center"
                >
                  <LucideEdit class="w-4 h-4 mr-1" /> Edit
                </button>
                <button 
                  @click="confirmDelete(user.id)" 
                  class="bg-red-500 text-white px-3 py-1 rounded-md hover:bg-red-600 transition flex items-center"
                >
                  <LucideTrash2 class="w-4 h-4 mr-1" /> Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
  
      
      <div v-if="showCreateUserModal" class="modal-overlay">
        <div class="modal-content">
          <h3 class="modal-title">Create User</h3>
          <form @submit.prevent="createUser" class="space-y-3">
            <input v-model="newUser.username" type="text" placeholder="User Name" required class="input-field">
            <input v-model="newUser.email" type="email" placeholder="Email" required class="input-field">
            <input v-model="newUser.password" type="password" placeholder="Password" required class="input-field">
            <select v-model="newUser.role" class="input-field">
              <option value="admin">Admin</option>
              <option value="manager">Manager</option>
              <option value="employee">Employee</option>
            </select>
            <div class="flex justify-end space-x-2">
              <button type="button" @click="showCreateUserModal = false" class="cancel-btn">Cancel</button>
              <button type="submit" class="submit-btn">Create</button>
            </div>
          </form>
        </div>
      </div>
  
    
      <div v-if="showEditUserModal" class="modal-overlay">
        <div class="modal-content">
          <h3 class="modal-title">Edit User</h3>
          <form @submit.prevent="updateUser" class="space-y-3">
            <input v-model="editUserData.username" type="text" placeholder="User Name" required class="input-field">
            <input v-model="editUserData.email" type="email" placeholder="Email" required class="input-field">
            <select v-model="editUserData.role" class="input-field">
              <option value="admin">Admin</option>
              <option value="manager">Manager</option>
              <option value="employee">Employee</option>
            </select>
            <div class="flex justify-end space-x-2">
              <button type="button" @click="showEditUserModal = false" class="cancel-btn">Cancel</button>
              <button type="submit" class="submit-btn">Update</button>
            </div>
          </form>
        </div>
      </div>
  
    </div>
  </template>

<script>
import { LucideUsers, LucideUserPlus, LucideEdit, LucideTrash2 } from 'lucide-vue-next';

export default {
    components: {
    LucideUsers,
    LucideUserPlus,
    LucideEdit,
    LucideTrash2,
  },
    data() {
        return {
            users: [],
            showCreateUserModal: false,
            showEditUserModal: false,
            newUser: {
                username: '',
                email: '',
                password: '',
                role: 'employee',
            },
            editUserData: {
                id: null,
                username: '',
                email: '',
                role: '',
            },
        };
    },
    methods: {
        async fetchUsers() {
            try {
                const response = await this.$api.getUsers();
                this.users = response.data;
            } catch (error) {
                console.error('Error fetching users:', error);
            }
        },
        async createUser() {
            try {
                await this.$api.createUser(this.newUser);
                this.showCreateUserModal = false;
                this.newUser = { username: '', email: '', password: '', role: 'employee' }; 
                this.fetchUsers();
            } catch (error) {
                console.error('Error creating user:', error);
            }
        },
        async deleteUser(id) {
            try {
                await this.$api.deleteUser(id);
                this.fetchUsers();
            } catch (error) {
                console.error('Error deleting user:', error);
            }
        },
        openEditModal(user) {
        this.editUserData = {
            id: user.id,
            username: user.username,
            email: user.email,
            role: user.role,
        };
        this.showEditUserModal = true;
    },
    async updateUser() {
        try {
             await this.$api.updateUser(this.editUserData.id,this.editUserData);
            this.showEditUserModal = false;
            this.fetchUsers();
        } catch (error) {
            console.error('Error updating user:', error);
        }
    },
        confirmDelete(id) {
            if (confirm('Are you sure you want to delete this user?')) {
                this.deleteUser(id);
            }
        },
    },
    created() {
        this.fetchUsers();
    },
};
</script>

<style>
.modal-overlay {  
  position: fixed;  
  top: 0;  
  left: 0;  
  right: 0;  
  bottom: 0;  
  display: flex;  
  align-items: center;  
  justify-content: center;  
  background-color: rgba(0, 0, 0, 0.5); /* bg-black bg-opacity-50 */  
}  

.modal-content {  
  background-color: #fff; /* bg-white */  
  padding: 1.5rem; /* p-6 (باعتبار 1rem = 16px) */  
  border-radius: 0.5rem; /* rounded-lg */  
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* shadow-lg (هذه قيمة مقدرة) */  
  width: 24rem; /* w-96 (96 * 0.25rem = 24rem) */  
}  

.modal-title {  
  font-size: 1.25rem; /* text-xl (باعتبار 1rem = 16px) */  
  font-weight: 600; /* font-semibold */  
  margin-bottom: 1rem; /* mb-4 (باعتبار 1rem = 16px) */  
}  

.input-field {  
  width: 100%; /* w-full */  
  padding: 0.5rem; /* p-2 (باعتبار 1rem = 16px) */  
  border: 1px solid #D1D5DB; /* border border-gray-300 (قيمة مقدرة لـ gray-300) */  
  border-radius: 0.5rem; /* rounded-lg */  
  outline: none; /* focus:outline-none */  
}  

.input-field:focus {  
  box-shadow: 0 0 0 2px #60A5FA; /* focus:ring-2 focus:ring-blue-500 (قيمة مقدرة لـ blue-500) */  
}  

.submit-btn {  
  background-color: #2563EB; /* bg-blue-600 (قيمة مقدرة لـ blue-600) */  
  color: #fff; /* text-white */  
  padding: 0.5rem 1rem; /* px-4 py-2 (باعتبار 1rem = 16px) */  
  border-radius: 0.5rem; /* rounded-lg */  
  transition: background-color 0.15s ease-in-out; /* transition */  
}  

.submit-btn:hover {  
  background-color: #1D4ED8; /* hover:bg-blue-700 (قيمة مقدرة لـ blue-700) */  
}  

.cancel-btn {  
  background-color: #E5E7EB; /* bg-gray-300 (قيمة مقدرة لـ gray-300) */  
  color: #4B5563; /* text-gray-700 (قيمة مقدرة لـ gray-700) */  
  padding: 0.5rem 1rem; /* px-4 py-2 (باعتبار 1rem = 16px) */  
  border-radius: 0.5rem; /* rounded-lg */  
  transition: background-color 0.15s ease-in-out; /* transition */  
}  

.cancel-btn:hover {  
  background-color: #D1D5DB; /* hover:bg-gray-400 (قيمة مقدرة لـ gray-400) */  
}  
</style>