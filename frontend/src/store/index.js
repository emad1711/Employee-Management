import { createStore } from 'vuex';
import axios from 'axios'; 


export default createStore({
    state: {
        token: localStorage.getItem('token') || null, 
        user: JSON.parse(localStorage.getItem('user')) || null, 
    },
    mutations: {
        
        SET_TOKEN(state, token) {
            state.token = token;
            localStorage.setItem('token', token); 
        },
     
        SET_USER(state, user) {
            state.user = user;
            localStorage.setItem('user', JSON.stringify(user)); 
        },
      
        CLEAR_AUTH(state) {
            state.token = null;
            state.user = null;
            localStorage.removeItem('token'); 
            localStorage.removeItem('user'); 
        },
    },
    actions: {
       
        async login({ commit }, credentials) {
         
                
                const response = await axios.post('http://127.0.0.1:8000/api/token-auth/', credentials);
               
                commit('SET_TOKEN', response.data.token);

                
                const userResponse = await axios.get('http://127.0.0.1:8000/api/users/', {
                    headers: { Authorization: `Token ${response.data.token}` }, 
                });
               
                commit('SET_USER', userResponse.data[0]); 
                return response;
           
        },
       
        async logout({ commit }) {
            try {
                
                await axios.post('http://127.0.0.1:8000/api/logout/',{} ,{
                    headers: { Authorization: `Token ${localStorage.getItem('token')}` },
                });
            } catch (error) {
                console.error('Logout error:', error); 
            }
         
            commit('CLEAR_AUTH');
          
            localStorage.clear();
        },
    },
    getters: {
        
        isAuthenticated(state) {
            return !!state.token; 
        },
      
        currentUser(state) {
            return state.user; 
        },
    },
});