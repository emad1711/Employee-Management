import { createApp } from 'vue'; 
import App from './App.vue'; 
import store from './store';
import router from './router'; 
import api from './api';



const app = createApp(App);



app.config.globalProperties.$api = api;

app.use(store);
app.use(router);



app.mount('#app');