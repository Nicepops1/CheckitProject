<template>
    <div class="navbar">
        <div class="left-side-components">
            <img class="globe" src="../assets/img/icons/internet-svgrepo-com.svg" alt="">
            <div class="text">
                <span>Достопримечательности</span>
                <span>России</span>
            </div>
        </div>
        <div class="right-side-components">
            <div @click="$router.push('/')" class="reference">Города</div>
            <div @click="$router.push('/map')" class="reference">Карта</div>
            <div @click="$router.push('/addplace')" class="reference">Добавить место</div>
            <div @click="$router.push('/signup')" class="reference">Регистрация</div>
            <div @click="$router.push('/signin')" class="reference enter-btn"><img src="../assets/img/icons/user_icon_179525.svg" alt="#"><span style="margin-left: .4rem">Войти</span></div>
        </div>
    </div>
</template>

<script>
export default{

}

</script>

<style scoped>


/* Import fonts */
@import url('../assets/fonts/fonts.css');

.navbar{
    position: sticky;
    top: 0rem;
    min-width: 100%;
    height: 3.75rem;
    border-bottom: 2px grey solid;
    display:inline-flex;
    flex-direction: row;
    padding-left: 7.5rem;
    padding-right: 7.5rem;
}
.left-side-components{
    display: flex;
    flex-direction: row;
}
.globe{
    width: 3.125rem;
    height: 3.125rem;
    margin-top: .24rem;
}
.text{
    display: flex;
    font-family: 'Inter-Regular';
    font-size: 20px;
    flex-direction: column;
    margin-left: .5rem;
    margin-top: .375rem;
}
.right-side-components{
    display: flex;
    flex-direction: row;
    margin-left: auto;
    justify-content: center;
    align-items: center;
    align-content: center;
}
.reference{
    cursor: pointer;
    font-family: 'FiraSans-Light';
    font-size: 22px;
    text-align: center;
    margin-left: 1.5625rem;
}
.enter-btn{
    display: flex;
    justify-content: center;
    align-items: center;
    align-content: center; 
}
@media screen and (max-width: 1280px) {
    
}
@media screen and (max-width: 860px) {
    .navbar{
        padding-left: .5rem;
        padding-right: .5rem;
        height: 2.8rem;
    }
    .reference{
        font-size: 14px;
        margin-left: .2rem;
    }
    .text{
        font-size: 16px;
        margin-top: .2rem;
    }
    .globe{
        width: 2.5rem;
        height: 2.5rem;
        margin-top: .1rem;
    }
}
</style>