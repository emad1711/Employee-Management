import axios from 'axios';
import store from '@/store';

const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/',
    headers: {
        'Content-Type': 'application/json',
    },
});


apiClient.interceptors.request.use((config) => {
    const token = store.state.token;
    if (token) {
        config.headers.Authorization = `Token ${token}`;
    }
    return config;
});

export default {
    login(email, password) {
        return apiClient.post('/token-auth/', { email, password });
    },
    logout() {
        return apiClient.post('/logout/');
    },
    getUsers() {
        return apiClient.get('/users/');
    },
    getCompanies() {
        return apiClient.get('/companies/');
    },
    createCompany(data) {
        return apiClient.post('/companies/', data);
    },
    updateCompany(id, data) {
        return apiClient.put(`/companies/${id}/`, data);
    },
    deleteCompany(id) {
        return apiClient.delete(`/companies/${id}/`);
    },
    getDepartments() {
        return apiClient.get('/departments/');
    },
    createDepartment(data) {
        return apiClient.post('/departments/', data);
    },
    updateDepartment(id, data) {
        return apiClient.put(`/departments/${id}/`, data);
    },
    deleteDepartment(id) {
        return apiClient.delete(`/departments/${id}/`);
    },
    getEmployees() {
        return apiClient.get('/employees/');
    },
    createEmployee(user) {
        return apiClient.post('/employees/', user);
    },
    updateEmployee(id, user) {
        return apiClient.put(`/employees/${id}/`, user);
    },
    deleteEmployee(id) {
        return apiClient.delete(`/employees/${id}/`);
    },
    createUser(user) {
        return apiClient.post('/users/', user);
    },
    updateUser(id, user) {
        return apiClient.put(`/users/${id}/`, user);
    },
    deleteUser(id) {
        return apiClient.delete(`/users/${id}/`);
    },
};