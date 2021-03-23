<template>
  <div class="hello">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark ">
          <router-link class="navbar-brand" to="/">Home</router-link>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse justify-content-center" id="navbarNav">
            <ul class="navbar-nav" v-if="!user">
              <li class="nav-item">
                <router-link class="nav-link" to="/login">Login</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/register">créer un compte</router-link>
              </li>
            </ul>
            <ul class="navbar-nav" v-if="user">
              <li class="nav-item">
                <a href ="javascript:void(0)" @click="deconnexion" class="nav-link">Deconnexion</a>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/userlists">liste</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/edition">edition</router-link>
              </li>
            </ul>
          </div>
        </nav>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
 export default {
  name: 'navbar',
  methods:{
    deconnexion(){
      localStorage.removeItem('token');
      this.$store.dispatch('user',null);
      this.$router.push('/login');
    }
  },
  computed : {
    ...mapGetters(['user'])
  }
}
</script>

<style>

</style>
