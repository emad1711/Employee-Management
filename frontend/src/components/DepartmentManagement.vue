<template>
    <div class="p-10 overflow-x-auto mt-6 w-full">
      <h2 class="text-2xl font-semibold text-gray-800 mb-4 flex items-center">
        <LucideBuilding class="w-6 h-6 mr-2" />
        Department Management
      </h2>
      
      <button @click="showCreateDepartmentModal = true" class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition">
        + Create Department
      </button>
  
      <div class="overflow-x-auto mt-6">
        <table class="min-w-full bg-white shadow-md rounded-lg">
          <thead >
            <tr class="bg-gray-800 text-white">
              <th class="py-3 px-4 text-center">ID</th>
              <th class="py-3 px-4 text-center">Name</th>
              <th class="py-3 px-4 text-center">Company</th>
              <th class="py-3 px-4 text-center">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="department in departments" :key="department.id" class="border-t">
              <td class="p-2 text-center">{{ department.id }}</td>
              <td class="p-2 text-center">{{ department.name }}</td>
              <td class="p-2 text-center">{{ department.company }}</td>
              <td class="p-2 text-center  space-x-2">
                <button @click="openEditModal(department)" class="px-3 py-1 bg-yellow-500 text-white rounded-md hover:bg-yellow-600 transition">
                  Edit
                </button>
                <button @click="confirmDelete(department.id)" class="px-3 py-1 bg-red-500 text-white rounded-md hover:bg-red-600 transition">
                  Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
  
     
      <div v-if="showCreateDepartmentModal" class="fixed inset-0 flex items-center justify-center bg-gray-900 bg-opacity-50">
        <div class="bg-white p-6 rounded-lg w-1/3">
          <h3 class="text-xl font-semibold mb-4">Create Department</h3>
          <form @submit.prevent="createDepartment" class="space-y-2">
            <input v-model="newDepartment.name" type="text" placeholder="Name" required class="input-field" />
            <select v-model="newDepartment.company" class="input-field">
              <option v-for="company in companies" :key="company.id" :value="company.id">
                {{ company.name }}
              </option>
            </select>
            <div class="flex space-x-2">
              <button type="submit" class="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition">
                Create
              </button>
              <button @click="showCreateDepartmentModal = false" class="px-4 py-2 bg-gray-400 text-white rounded-lg hover:bg-gray-500 transition">
                Cancel
              </button>
            </div>
          </form>
        </div>
      </div>
  
      <div v-if="showEditDepartmentModal" class="fixed inset-0 flex items-center justify-center bg-gray-900 bg-opacity-50">
        <div class="bg-white p-6 rounded-lg w-1/3">
          <h3 class="text-xl font-semibold mb-4">Edit Department</h3>
          <form @submit.prevent="updateDepartment" class="space-y-2">
            <input v-model="editDepartmentData.name" type="text" placeholder="Name" required class="input-field" />
            <select v-model="editDepartmentData.company" class="input-field">
              <option v-for="company in companies" :key="company.id" :value="company.id">
                {{ company.name }}
              </option>
            </select>
            <div class="flex space-x-2">
              <button type="submit" class="px-4 py-2 bg-yellow-600 text-white rounded-lg hover:bg-yellow-700 transition">
                Update
              </button>
              <button @click="showEditDepartmentModal = false" class="px-4 py-2 bg-gray-400 text-white rounded-lg hover:bg-gray-500 transition">
                Cancel
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>

<script>
import { LucideBuilding } from 'lucide-vue-next';
export default {
    components: { LucideBuilding },
    data() {
        return {
            departments: [],
            companies: [],
            showCreateDepartmentModal: false,
            showEditDepartmentModal: false,
            newDepartment: {
                name: '',
                company: null,
            },
            editDepartmentData: {
                id: null,
                name: '',
                company: null,
            },
        };
    },
    methods: {
        async fetchDepartments() {
            try {
                const response = await this.$api.getDepartments();
                this.departments = response.data;
            } catch (error) {
                console.error('Error fetching departments:', error);
            }
        },
        async fetchCompanies() {
            try {
                const response = await this.$api.getCompanies();
                this.companies = response.data;
            } catch (error) {
                console.error('Error fetching companies:', error);
            }
        },
        async createDepartment() {
            try {
                await this.$api.createDepartment(this.newDepartment);
                this.showCreateDepartmentModal = false;
                this.newDepartment = { name: '', company: null }; 
                this.fetchDepartments();
            } catch (error) {
                console.error('Error creating department:', error);
            }
        },
        async deleteDepartment(id) {
            try {
                await this.$api.deleteDepartment(id);
                this.fetchDepartments();
            } catch (error) {
                console.error('Error deleting department:', error);
            }
        },
        openEditModal(department) {
            this.editDepartmentData = { ...department }; 
            this.showEditDepartmentModal = true;
        },
        async updateDepartment() {
            try {
                await this.$api.updateDepartment(this.editDepartmentData.id, this.editDepartmentData);
                this.showEditDepartmentModal = false;
                this.fetchDepartments();
            } catch (error) {
                console.error('Error updating department:', error);
            }
        },
        confirmDelete(id) {
            if (confirm('Are you sure you want to delete this department?')) {
                this.deleteDepartment(id);
            }
        },
    },
    created() {
        this.fetchDepartments();
        this.fetchCompanies();
    },
};
</script>

<style>
.input-field {
  @apply w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-400 outline-none;
}
</style>