<template>
    <div class="app">
        <navbar></navbar>
        <router-view class="start"></router-view>
    </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
export default{
  components: { 
        Navbar 
    },
    
}

</script>

<style>
*{
    overflow-x: hidden;
}
.label{
    font-family: 'FiraSans-Bold';
    height: auto;
    overflow-y: hidden;
    margin-bottom: 1rem;
}
</style>