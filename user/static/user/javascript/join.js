
var register = new Vue({
    el: '#register',
    data: {
        username: '',
        password: ''
    },
    methods: {
        join: function (event) {
            if (this.username.length == 0 || this.password.length == 0) {
                vant.Toast('用户名密码不能为空');
            } else {
                apiJoin({'username' : this.username, 'password' : this.password}).then(res => {
                    location.href = '/login';
                });
            }
        }
    }
})

