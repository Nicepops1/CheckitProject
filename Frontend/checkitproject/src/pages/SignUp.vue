<template>
    <div class="container">
        <form @submit.prevent action="">
            <h1 class="label">Регистрация</h1>
            <p class="hint">ИМЯ ПОЛЬЗОВАТЕЛЯ</p>
            <input v-bind:value="Nickname" @input="inputNickname" type="text" class="form-input">
            <p class="hint">ЛОГИН</p>
            <input v-bind:value="LoginName" @input="inputLogin" type="text" class="form-input">
            <p class="hint">ПАРОЛЬ</p>
            <input v-bind="Password" @input="inputPassword" type="password" class="form-input">
            <button @click="Register" class="up-btn">ЗАРЕГИСТРИРОВАТСЯ</button>
        </form>
    </div>
</template>

<script>
import $ from 'jquery'
export default{

    data() {
        return {
            Nickname : '',
            LoginName : '',
            Password : '',
            Id : undefined,
        }
    },
    methods : {
        Register() {
            if (this.LoginName.length>12) {
                alert("Логин не должен быть длинее 12 символов!")
            }else if (this.LoginName.length<4){
                alert("Логин не должен быть короче 4 символов!")
            }else {
                $.ajax({
                url: "http://127.0.0.1:8000/auth/users/",
                type: "POST",
                data: {
                    username: this.LoginName,
                    password: this.Password
                },
                headers:{
                        "Access-Control-Allow-Origin" : '*',
                },
                success: () => {
                    this.Login()
                },
                error: (data) => {
                    if (data.responseJSON.password) {
                    alert(data.responseJSON.password[0])
                    } else if (data.responseJSON.username) {
                    alert(data.responseJSON.username[0])
                    }
                }
                })
            }
        },
        Login() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login/",
                    type: "POST",
                    data: {
                        username: this.LoginName,
                        password: this.Password
                    },
                    headers:{
                        "Access-Control-Allow-Origin" : '*',
                    },
                    success: (response) => {
                        this.Token = response.auth_token
                        sessionStorage.setItem("AuthToken", this.Token)
                        sessionStorage.setItem("Nickname", this.Nickname)
                        this.GetId()
                        this.ChangeNickname()
                        this.$router.push('/account')
                    },
                    error: (data) => {
                        alert(data.responseJSON.non_field_errors[0])
                    }
                })
                },
            GetId(){
                $.ajax({
                    url: 'http://127.0.0.1:8000/auth/users/me',
                    type: 'GET',
                    headers:{
                        'Authorization' : 'Token' + sessionStorage.getItem('AuthToken'),
                    },
                    success: (response) => {
                        this.Id = response.data.id;
                        sessionStorage.setItem('Id', this.Id)
                    },
                    error: (data) => {
                        alert(data.responseJSON.non_field_errors[0])
                    }
                })
            },
            ChangeNickname(){
                $.ajax({
                    url : 'http://127.0.0.1:8000/profile/',
                    type: 'POST',
                    headers : {
                            'Authorization' : 'Token' + sessionStorage.getItem('AuthToken'),
                    },
                    data: {
                        user: sessionStorage.getItem('Id'),
                        user_name : this.Nickname,
                    },
                    success: (response) => {},
                    error : (data) => {
                        alert(data.responseJSON.non_field_errors[0])
                    }
                })
            },
        inputNickname(event) {
            this.Nickname = event.target.value;
        },
        inputLogin(event) {
            this.LoginName = event.target.value;
        },
        inputPassword(event){
            this.Password = event.target.value;
        },

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


.hint{
    font-family: 'FiraSans-Light';
    margin-bottom: 0.9375rem;
    margin-top: 1.875rem;
    overflow-y: hidden;
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