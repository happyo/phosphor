var user = new Vue({
    el: '#user',
    data: {
        username: '',
        password: ''
    },
    methods: {
        login: function (event) {
            if (this.username.length == 0 || this.password.length == 0) {
                vant.Toast('用户名密码不能为空');
            } else {
                apiSignIn({'username' : this.username, 'password' : this.password}).then(res => {
                    var data = res['data'];
                    var username = data['username'];
                    location.href = '/' + username + '/todos';
                });
            }
        },
        register: function (event) {
            location.href = '/join';
        }
    }
})
