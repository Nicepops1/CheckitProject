<template>
    <div class="fullpage">
        <div class="bground-btn">
            <button class="btn-down"></button>
        </div>
        <town-array-vue></town-array-vue>
    </div>
</template>

<script>
import TownArrayVue from '../components/TownArray.vue'

export default{
    components: {
        TownArrayVue,
    }
}

</script>

<style scooped>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
.fullpage{
    position: absolute;
    overflow-y: auto;
    width: 100%;
    height: calc(100vh - 3.75rem);
}
.bground-btn{
    width: 100%;
    height: 60rem;
    display: inline-flex;
    flex-direction: column-reverse;
    background: url('../assets/img/BMain.jpg');
    background-size: cover;
    background-size: 120rem 60rem;
    border-bottom: 2px grey solid;
    padding-bottom: 1rem;
}
.btn-down{
    width: 3.125rem;
    height: 3.125rem;
    background: url('../assets/img/icons/down-arrow-svgrepo-com.svg');
    border: none;
    align-self: center;
}

@media screen and (max-width: 1280px) {
    .bground-btn{
    width: calc(120rem * 2/3 - 1rem);
    height: calc(60rem * .56);
    padding-bottom: 1.5rem;
    display: inline-flex;
    flex-direction: column-reverse;
    
    overflow-x: hidden;
    background-size: calc(120rem * 2/3 * .84) calc(63.75rem * .6 * .84);
    background-repeat: no-repeat;
    background-position-x:center;
}
.btn-down{
    width: calc(3.125rem * 2/3);
    height: calc(3.125rem * 2/3);
    border: none;
    align-self: center;
}
}
</style>