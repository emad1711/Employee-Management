
import { createRouter, createWebHistory } from 'vue-router';
import TheLogin from '../components/Login.vue';
import TheDashboard from '@/components/Dashboard.vue';

import UserManagement from '@/components/UserManagement.vue';
import CompanyManagement from '@/components/CompanyManagement.vue';
import DepartmentManagement from '@/components/DepartmentManagement.vue';
import EmployeeManagement from '@/components/EmployeeManagement.vue';
import store from '@/store';



const routes = [
    { path: '/', component: TheLogin },
    { path: '/dashboard', component: TheDashboard, meta: { requiresAuth: true } },
    { path: '/users', component: UserManagement, meta: { requiresAuth: true } },
    { path: '/companies', component: CompanyManagement, meta: { requiresAuth: true } },
    { path: '/departments', component: DepartmentManagement, meta: { requiresAuth: true } },
    { path: '/employees', component: EmployeeManagement, meta: { requiresAuth: true } },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    const isAuthenticated = store.getters.isAuthenticated;
    if (to.meta.requiresAuth && !isAuthenticated) {
        next('/'); 
    } else {
        next(); 
    }
});

export default router;