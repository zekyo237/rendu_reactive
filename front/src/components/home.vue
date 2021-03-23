<template>
  <div>
  <h3 v-if="user">Bon retour parmis nous {{user.username}}</h3>
  <h3 v-if="!user">Veuillez vous authentifier</h3>
  </div>
</template>
<script>
import {mapGetters} from 'vuex'
export default {
  name:'home',
  computed : {
    ...mapGetters(['user'])
  }
}

</script>
<style scoped>

</style>