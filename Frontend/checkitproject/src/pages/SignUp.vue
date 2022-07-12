<template>
    <div class="container">
        <form action="">
            <h1 class="label">Регистрация</h1>
            <p class="hint">ИМЯ ПОЛЬЗОВАТЕЛЯ</p>
            <input type="text" class="form-input">
            <p class="hint">E-MAIL</p>
            <input type="text" class="form-input">
            <p class="hint">ПАРОЛЬ</p>
            <input type="password" class="form-input">
            <p class="hint">ПОВТОРИТЕ ПАРОЛЬ</p>
            <input type="password" class="form-input">
            <button class="up-btn">ЗАРЕГИСТРИРОВАТСЯ</button>
        </form>
    </div>
</template>

<script>
export default{

}

</script>

<style scooped>

@import url('../assets/fonts/fonts.css');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}


.hint{
    font-family: 'FiraSans-Light';
    margin-bottom: 0.9375rem;
    margin-top: 1.875rem;
}
.form-input{
    background: #FFFFFF;
    border: 1px solid #000000;
    border-radius: 15px;
    width: 35.625rem;
    height: 4.6875rem;
}
form{
    display: flex;
    align-content: center;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}
.container{
    top: 3.75rem;
    padding-bottom: 1rem;
    position: absolute;
    width: 100%;
    height: 100vh;
    display: flex;
    align-content: center;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    overflow-y: auto;
}
.up-btn{
    width: 15.625rem;
    height: 3.125rem;
    font-family: 'FiraSans-Light';
    font-size: 22px;
    background: #FFFFFF;
    border: 1px solid #000000;
    border-radius: 15px;
    margin-top: .9375rem;
}

@media screen and (max-width: 1280px) {
    .signup-label{
    font-family: 'FiraSans-Bold';    
}
.hint{
    font-family: 'FiraSans-Light';
    margin-bottom: calc(0.9375rem * 2/3);
    margin-top: calc(1.875rem * 2/3);
}
.form-input{
    background: #FFFFFF;
    border: 1px solid #000000;
    border-radius: 15px;
    width: calc(35.625rem * 2/3);
    height: calc(4.6875rem * 2/3);
}
form{
    display: flex;
    align-content: center;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}
.container{
    width: 100%;
    height: calc(100vh - 3.75rem);
    display: flex;
    align-content: center;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}
.up-btn{
    width: calc(15.625rem * 2/3);
    height: calc(3.125rem * 2/3);
    font-family: 'FiraSans-Light';
    font-size: calc(22px * 2/3);
    background: #FFFFFF;
    border: 1px solid #000000;
    border-radius: 15px;
    margin-top: calc(.9375rem * 2/3);
}
}
</style>