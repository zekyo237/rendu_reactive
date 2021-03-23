<template>
  <div>
   <div class="card-body">
  <ul>
      <h3>Liste utilisateur 1</h3>
      
      <li v-for="utilisateur in this.userlist.Utilisateur1" :key="utilisateur.id">
        <div class="card w-75">
       <div class="card-body">
      <h5 class="card-title">{{utilisateur.username}}</h5>
      
    
  </div>
</div> 
       </li>
    </ul>
    </div>
    <ul>
      <h3>Liste utilisateur 2</h3>
      <li v-for="utilisateur in this.userlist.Utilisateur2" :key="utilisateur.id">
         <div class="card w-75">
       <div class="card-body">
      <h5 class="card-title">{{utilisateur.username}}</h5>
    
    </div>
    </div> 
       </li>
    </ul>
    <ul>
      <h3>Liste utilisateur 3</h3>
      <li v-for="utilisateur in this.userlist.Utilisateur3" :key="utilisateur.id">
         <div class="card w-75">
       <div class="card-body">
      <h5 class="card-title">{{utilisateur.username}}</h5>
      
      </div>
      </div> 
       </li>
    </ul>
  
  
  </div>
  
</template>
<script>
import axios from 'axios' 
export default {
    name: "userlists",
    data(){
        return{
            userlist:[]
        }
    },
    mounted(){
       
          axios.get('getalluser')
          .then(response=>{
            this.userlist= response.data
            console.log(response.data)
          })
          .catch(error =>{
            console.log(error)
          })
           
         

         
    }
}
</script>

<style scoped>

</style>