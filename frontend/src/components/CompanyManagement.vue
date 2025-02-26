<template>
    <div class="p-10 overflow-x-auto mt-6 w-full">
      <h2 class="text-2xl font-semibold text-gray-800 mb-4 flex items-center">
        <LucideBuilding class="w-6 h-6 mr-2" /> Company Management
      </h2>
  
   
      <button 
        @click="showCreateCompanyModal = true"
        class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition flex items-center"
      >
        <LucidePlus class="w-5 h-5 mr-2" /> Create Company
      </button>
  
   
      <div class="overflow-x-auto mt-6">
        <table class="min-w-full bg-white shadow-md rounded-lg">
          <thead>
            <tr class="bg-gray-800 text-white">
              <th class="py-3 px-4 text-center">ID</th>
              <th class="py-3 px-4 text-center">Name</th>
              <th class="py-3 px-4 text-center">Departments</th>
              <th class="py-3 px-4 text-center">Employees</th>
              <th class="py-3 px-4 text-center">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="company in companies" :key="company.id" class="border-b hover:bg-gray-100 transition">
              <td class="py-3 px-4 text-center">{{ company.id }}</td>
              <td class="py-3 px-4 text-center">{{ company.name }}</td>
              <td class="py-3 px-4 text-center">{{ company.department_count }}</td>
              <td class="py-3 px-4 text-center">{{ company.employee_count }}</td>
              <td class="py-3 px-4 text-center flex justify-center space-x-4">
                <button 
                  @click="openEditModal(company)" 
                  class="bg-yellow-500 text-white px-3 py-1 rounded-md hover:bg-yellow-600 transition flex items-center"
                >
                  <LucideEdit class="w-4 h-4 mr-1" /> Edit
                </button>
                <button 
                  @click="confirmDelete(company.id)" 
                  class="bg-red-500 text-white px-3 py-1 rounded-md hover:bg-red-600 transition flex items-center"
                >
                  <LucideTrash2 class="w-4 h-4 mr-1" /> Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
  
     
      <div v-if="showCreateCompanyModal" class="modal-overlay">
        <div class="modal-content">
          <h3 class="modal-title">Create Company</h3>
          <form @submit.prevent="createCompany" class="space-y-3">
            <input v-model="newCompany.name" type="text" placeholder="Company Name" required class="input-field">
            <div class="flex justify-end space-x-2">
              <button type="button" @click="showCreateCompanyModal = false" class="cancel-btn">Cancel</button>
              <button type="submit" class="submit-btn">Create</button>
            </div>
          </form>
        </div>
      </div>
  
      
      <div v-if="showEditCompanyModal" class="modal-overlay">
        <div class="modal-content">
          <h3 class="modal-title">Edit Company</h3>
          <form @submit.prevent="updateCompany" class="space-y-3">
            <input v-model="editCompanyData.name" type="text" placeholder="Company Name" required class="input-field">
            <div class="flex justify-end space-x-2">
              <button type="button" @click="showEditCompanyModal = false" class="cancel-btn">Cancel</button>
              <button type="submit" class="submit-btn">Update</button>
            </div>
          </form>
        </div>
      </div>
  
    </div>
  </template>

<script>
import { LucideBuilding, LucidePlus, LucideEdit, LucideTrash2 } from 'lucide-vue-next';
export default {
    components: {
    LucideBuilding,
    LucidePlus,
    LucideEdit,
    LucideTrash2,
  },
    data() {
        return {
            companies: [],
            showCreateCompanyModal: false,
            showEditCompanyModal: false,
            newCompany: {
                name: '',
            },
            editCompanyData: {
                id: null,
                name: '',
            },
        };
    },
    methods: {
        async fetchCompanies() {
            try {
                const response = await this.$api.getCompanies();
                this.companies = response.data;
            } catch (error) {
                console.error('Error fetching companies:', error);
            }
        },
        async createCompany() {
            try {
                await this.$api.createCompany(this.newCompany);
                this.showCreateCompanyModal = false;
                this.newCompany = { name: '' };
                this.fetchCompanies();
            } catch (error) {
                console.error('Error creating company:', error);
            }
        },
        async deleteCompany(id) {
            try {
                await this.$api.deleteCompany(id);
                this.fetchCompanies();
            } catch (error) {
                console.error('Error deleting company:', error);
            }
        },
        openEditModal(company) {
            this.editCompanyData = { ...company };
            this.showEditCompanyModal = true;
        },
        async updateCompany() {
            try {
                await this.$api.updateCompany(this.editCompanyData.id, this.editCompanyData);
                this.showEditCompanyModal = false;
                this.fetchCompanies();
            } catch (error) {
                console.error('Error updating company:', error);
            }
        },
        confirmDelete(id) {
            if (confirm('Are you sure you want to delete this company?')) {
                this.deleteCompany(id);
            }
        },
    },
    created() {
        this.fetchCompanies();
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