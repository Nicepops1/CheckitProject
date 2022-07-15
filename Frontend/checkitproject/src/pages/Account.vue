<template>
    <div class="account">
        <img class="avatar-img" src="../assets/img/icons/user_icon_179525.svg" alt="">
        <button class="btn">ИЗМЕНИТЬ ФОТОГРАФИЮ ПРОФИЛЯ</button>
        <button @click="Logout" class="btn">ВЫЙТИ ИЗ УЧЕТНОЙ ЗАПИСИ</button>
  
  </div>
</template>

<script>
import $ from 'jquery'
export default{
    methods: {
        Logout() {
            $.ajax({
                url: 'http://127.0.0.1:8000/auth/token/logout',
                type: 'POST',
                headers : {
                    'Autorization' : 'Token' + sessionStorage.getItem('AuthToken'),
                },
                success: (response) => {
                    sessionStorage.setItem('AuthToken', '')
                    sessionStorage.setItem('Nickname', '')
                }

            })
        }
    }
}

</script>

<style scooped>
@import url('../assets/fonts/fonts.css');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
.avatar-img{
    width: 15.625rem;
}
.btn{
    width: 15.625rem;
    height: 3.125rem;
    font-family: 'FiraSans-Light';
    font-size: 20px;
    background: #FFFFFF;
    border: 1px solid #000000;
    border-radius: 15px;
    margin-top: .9375rem;
}
.account{
    display: flex;
    flex-direction: column;
    align-content: center;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: calc(100vh - 4rem);
}
</style>