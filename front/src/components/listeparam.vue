<template>
  <div>les informations relatives à la liste :{{$route.params.listeid}}  pour l 'utilisateur : {{$route.params.idUser}} sont {{this.donnee}}</div>
</template>
<script>
import axios from 'axios'
export default {
    name: "listeparam",
    data(){
        return{
            donnee:[]
        }
    },
    mounted(){
       
          axios.get('getusers/'+this.$route.params.listeid+'/'+this.$route.params.idUser)
          .then(response=>{
            
            this.donnee=response.data
          })
          .catch(error =>{
            console.log(error)
          })
           
    }  
}
</script>
<style scoped>

</style>