import Vue from 'vue'
import Router from 'vue-router'
import home from './components/home.vue'
import login from './components/login.vue'
import register  from './components/register.vue'
import userlists  from './components/userlists.vue'
import listeparam from './components/listeparam.vue'
import store from './vuex'

Vue.use(Router)

export  default  new Router({
    mode: 'history',
    routes: [
        
        
        { path: '/',component: home },
        { path: "/login",component: login },
        { path: "/register",component:register },
        {path:  "/listeuser/:listeid/:idUser",component: listeparam},
        {path:"/userlists",component:userlists ,
        beforeEnter(to,from,next){
            if(!store.getters.user){
                next('/login')
            }else{
                next()
            }
        }
    
    
    
    },
        { path: '*', redirect: '/' }
    ]
})
