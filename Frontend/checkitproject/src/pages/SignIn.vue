<template>
    <div class="container">
        <h1 class="label">Вход</h1>
        <p class="hint">ИМЯ ПОЛЬЗОВАТЕЛЯ</p>
        <input type="text" v-bind:value="Username" @input="inputUsername" class="form-input">
        <p class="hint">ПАРОЛЬ</p> 
        <input type="password" v-bind:value="Password" @keyup.enter="Login" @input="inputPassword" class="form-input">
        <button v-on:click="Login" class="up-btn">ВОЙТИ</button>
  </div>
</template>

<script>
import $ from 'jquery'
export default{
    data() {
        return {
            Username : '',
            Password : '',
            Token : '',
        };
    },
    methods: {
            Login() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login/",
                    type: "POST",
                    data: {
                    username: this.Username,
                    password: this.Password
                    },
                    headers:{
                        "Access-Control-Allow-Origin" : '*',
                    },
                    success: (response) => {
                        this.Token = response.auth_token
                        sessionStorage.setItem("AuthToken", this.Token)
                        sessionStorage.setItem("Username", this.Username)
                        this.$router.push('/account')
                    },
                    error: (data) => {
                        alert(data.responseJSON.non_field_errors[0])
                    }
                })
                },
    inputUsername(event) {
        this.Username = event.target.value;
    },
    inputPassword(event){
        this.Password = event.target.value;
    },
    mounted() {
        sessionStorage.setItem('AuthToken', "")
        sessionStorage.setItem('Username', "")
    },
}
}

</script>

<style scooped>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
</style>