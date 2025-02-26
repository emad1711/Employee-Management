<template>  
    <div class="p-10 overflow-x-auto mt-6 w-full">  
        <h2 class="text-3xl font-semibold text-gray-800 flex items-center mb-4">  
            <LucideUsers class="w-6 h-6 mr-2" />  
            Employee Management  
        </h2>  
  
        <button   
            @click="showCreateEmployeeModal = true"   
            class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
            :disabled="!isAdmin">  
            + Create Employee  
        </button>  
  
        <div class="overflow-x-auto mt-6">  
            <table class="min-w-full bg-white shadow-md rounded-lg">  
                <thead>  
                    <tr class="bg-gray-800 text-white">  
                        <th class="py-3 px-4 text-left">ID</th>  
                        <th class="py-3 px-4 text-left">Name</th>  
                        <th class="py-3 px-4 text-left">Email</th>  
                        <th class="py-3 px-4 text-left">Phone</th>  
                        <th class="py-3 px-4 text-left">Address</th>  
                        <th class="py-3 px-4 text-left">Job Title</th>  
                        <th class="py-3 px-6 text-left">Hire Date</th>  
                        <th class="py-3 px-4 text-left">Status</th>  
                        <th class="py-3 px-1 text-left">Work Days</th>  
                        <th class="py-3 px-1 text-left">Company</th>  
                        <th class="py-3 px-1 text-left">Department</th>  
                        <th class="py-3 px-4 text-center">Actions</th>  
                    </tr>  
                </thead>  
                <tbody>  
                    <tr v-for="employee in employees" :key="employee.id" class="border-t">  
                        <td class="p-2 text-center">{{ employee.id }}</td>  
                        <td class="p-2">{{ employee.name }}</td>  
                        <td class="p-2">{{ employee.email }}</td>  
                        <td class="p-2">{{ employee.phone_number }}</td>  
                        <td class="p-2">{{ employee.address }}</td>  
                        <td class="p-2">{{ employee.job_title }}</td>  
                        <td class="p-2">{{ employee.hire_date }}</td>  
                        <td class="p-2"><span>{{ employee.status }}</span></td>  
                        <td class="p-2">{{ employee.work_days }}</td>  
                        <td class="p-2">{{ employee.company }}</td>  
                        <td class="p-2">{{ employee.department }}</td>  
                        <td class="p-2 flex space-x-2">  
                            <button   
                                @click="openEditModal(employee)"   
                                class="px-3 py-1 bg-yellow-500 text-white rounded-md hover:bg-yellow-600 transition">  
                                Edit  
                            </button>  
                            <button   
                                @click="confirmDelete(employee.id)"   
                                class="px-3 py-1 bg-red-500 text-white rounded-md hover:bg-red-600 transition">  
                                Delete  
                            </button>  
                        </td>  
                    </tr>  
                </tbody>  
            </table>  
        </div>  
  
       
        <div v-if="showCreateEmployeeModal" class="fixed inset-0 flex items-center justify-center bg-gray-900 bg-opacity-50">  
            <div class="bg-white p-6 rounded-lg w-1/3">  
                <h3 class="text-xl font-semibold mb-4">Create Employee</h3>  
                <form @submit.prevent="createEmployee" class="space-y-2">  
                    <input v-model="newEmployee.name" type="text" placeholder="Name" required class="input-field" />  
                    <input v-model="newEmployee.email" type="email" placeholder="Email" required class="input-field" />  
                    <input v-model="newEmployee.phone_number" type="text" placeholder="Phone" required class="input-field" />  
                    <input v-model="newEmployee.address" type="text" placeholder="Address" required class="input-field" />  
                    <input v-model="newEmployee.job_title" type="text" placeholder="Job Title" required class="input-field" />  
                    <input v-model="newEmployee.hire_date" type="date" class="input-field" />  
                    <select v-model="newEmployee.status" class="input-field">  
                        <option value="pending">Pending</option>  
                        <option value="active">Active</option>  
                        <option value="inactive">Inactive</option>  
                    </select>  
                    <select v-model="newEmployee.company" class="input-field">  
                        <option v-for="company in companies" :key="company.id" :value="company.id">  
                            {{ company.name }}                        </option>  
                      </select>  
                      <select v-model="newEmployee.department" class="input-field">  
                          <option v-for="department in departments" :key="department.id" :value="department.id">  
                              {{ department.name }}  
                          </option>  
                      </select>  
                      <div class="flex space-x-2">  
                          <button type="submit" class="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition">  
                              Create  
                          </button>  
                          <button @click="showCreateEmployeeModal = false" class="px-4 py-2 bg-gray-400 text-white rounded-lg hover:bg-gray-500 transition">  
                              Cancel  
                          </button>  
                      </div>  
                  </form>  
              </div>  
          </div>  
  
         
          <div v-if="showEditEmployeeModal" class="fixed inset-0 flex items-center justify-center bg-gray-900 bg-opacity-50">  
              <div class="bg-white p-6 rounded-lg w-1/3">  
                  <h3 class="text-xl font-semibold mb-4">Edit Employee</h3>  
                  <form @submit.prevent="updateEmployee" class="space-y-2">  
                      <input v-model="editEmployeeData.name" type="text" placeholder="Name" required class="input-field" />  
                      <input v-model="editEmployeeData.email" type="email" placeholder="Email" required class="input-field" />  
                      <input v-model="editEmployeeData.phone_number" type="text" placeholder="Phone" required class="input-field" />  
                      <input v-model="editEmployeeData.address" type="text" placeholder="Address" required class="input-field" />  
                      <input v-model="editEmployeeData.job_title" type="text" placeholder="Job Title" required class="input-field" />  
                      <input v-model="editEmployeeData.hire_date" type="date" class="input-field" />  
                      <select v-model="editEmployeeData.status" class="input-field">  
                          <option value="pending">Pending</option>  
                          <option value="active">Active</option>  
                          <option value="inactive">Inactive</option>  
                      </select>  
                      <select v-model="editEmployeeData.company" class="input-field">  
                          <option v-for="company in companies" :key="company.id" :value="company.id">  
                              {{ company.name }}  
                          </option>  
                      </select>  
                      <select v-model="editEmployeeData.department" class="input-field">  
                          <option v-for="department in departments" :key="department.id" :value="department.id">  
                              {{ department.name }}  
                          </option>  
                      </select>  
                      <div class="flex space-x-2">  
                          <button type="submit" class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition">  
                              Update  
                          </button>  
                          <button @click="showEditEmployeeModal = false" class="px-4 py-2 bg-gray-400 text-white rounded-lg hover:bg-gray-500 transition">  
                              Cancel  
                          </button>  
                      </div>  
                  </form>  
              </div>  
          </div>  
      </div>  
  </template>  
  
  <script>  
  import { LucideUsers } from 'lucide-vue-next';  
  import { mapGetters } from 'vuex'; 
  export default {  
      components: { LucideUsers },  
      data() {  
          return {  
              employees: [],  
              companies: [],  
              departments: [],  
              showCreateEmployeeModal: false,  
              showEditEmployeeModal: false,  
              newEmployee: {  
                  name: '',  
                  email: '',  
                  phone_number: '',  
                  address: '',  
                  job_title: '',  
                  hire_date: '',  
                  status: 'pending',  
                  company: null,  
                  department: null,  
              },  
              editEmployeeData: {  
                  id: null,  
                  name: '',  
                  email: '',  
                  phone_number: '',  
                  address: '',  
                  job_title: '',  
                  hire_date: '',  
                  status: 'pending',  
                  company: null,  
                  department: null,  
              },  
         
          };  
      },  
      computed: {  
          ...mapGetters(['currentUser']),
      isAdmin() {  
          
        return this.currentUser.role === 'admin';  
      }  
    },
      methods: {  
          async fetchEmployees() {  
              try {  
                  const response = await this.$api.getEmployees();  
                  this.employees = response.data;  
              } catch (error) {  
                  console.error('Error fetching employees:', error);  
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
          async fetchDepartments() {  
              try {  
                  const response = await this.$api.getDepartments();  
                  this.departments = response.data;  
              } catch (error) {  
                  console.error('Error fetching departments:', error);  
              }  
          },  
          async createEmployee() {  
              try {  
                  await this.$api.createEmployee(this.newEmployee);  
                  this.showCreateEmployeeModal = false;  
                  this.newEmployee = {  
                      name: '',  
                      email: '',  
                      phone_number: '',  
                      address: '',  
                      job_title: '',  
                      hire_date: '',  
                      status: 'pending',  
                      company: null,  
                      department: null,  
                  }; 
                  this.fetchEmployees();  
              } catch (error) {  
                  console.error('Error creating employee:', error);  
              }  
          },  
          async deleteEmployee(id) {  
              try {  
                  await this.$api.deleteEmployee(id);  
                  this.fetchEmployees();  
              } catch (error) {  
                  console.error('Error deleting employee:', error);  
              }  
          },  
          openEditModal(employee) {  
              this.editEmployeeData = { ...employee }; 
              this.showEditEmployeeModal = true;  
          },  
          async updateEmployee() {  
              try {  
                  await this.$api.updateEmployee(this.editEmployeeData.id, this.editEmployeeData);  
                  this.showEditEmployeeModal = false;  
                  this.fetchEmployees();  
              } catch (error) {  
                  console.error('Error updating employee:', error);  
              }  
          },  
          confirmDelete(id) {  
              if (confirm('Are you sure you want to delete this employee?')) {  
                  this.deleteEmployee(id);  
              }  
          },  
      },  
      created() {  
          this.fetchEmployees();  
          this.fetchCompanies();  
          this.fetchDepartments();  
      },  
  };  
  </script>  
  
  <style>  
 .input-field {  
  width: 100%; /* w-full */  
  padding: 0.5rem; /* p-2 (باعتبار 1rem = 16px, إذا كان هذا هو إعدادك) */  
  border: 1px solid #D1D5DB; /* border border-gray-300 (نفترض أن gray-300 تعادل هذه القيمة اللونية) */  
  border-radius: 0.5rem; /* rounded-lg */  
  outline: none; /* outline-none */  
}  

.input-field:focus {  
  box-shadow: 0 0 0 2px rgba(96, 165, 250, 0.5); /* focus:ring-2 focus:ring-blue-400 (نفترض أن blue-400 تعادل هذه القيمة اللونية مع opacity 50%) */  
}  
  </style>