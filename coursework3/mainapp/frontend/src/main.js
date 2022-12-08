import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './style.css'
import App from './App.vue'
import About from './components/About.vue'
import Profile from './components/Profile.vue'
import Auctions from './components/Auctions.vue'
import NewAuction from './components/NewAuction.vue'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";

const routes = [
    { path: '/', name: 'Auctions', component: Auctions },
    { path: '/about', name: 'About', component: About },
    { path: '/new-auction', name: 'NewAuction', component: NewAuction },
    { path: '/profile', name: 'Profile', component: Profile },

    

]


const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHistory(),
    routes, // short for `routes: routes`
  })


const app = createApp(App)
// Make sure to _use_ the router instance to make the
// whole app router-aware.
app.use(router) 

app.mount('#app')

//createApp(App).mount('#app')
