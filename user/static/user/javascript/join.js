
var register = new Vue({
    el: '#register',
    data: {
        username: '',
        password: ''
    },
    methods: {
        join: function (event) {
            var params = new URLSearchParams();
            params.append('username', register.username);
            params.append('password', register.password);
            axios({
                method: 'post',
                url: '',
                data: params,
                headers: {
                    'Content-Type':'application/x-www-form-urlencoded'
                }
            }).then(function (response) {
                var data = response['data'];
                var code = data['code'];
                if (code == 0) {
                    var message = data['data']['errorMessage'];
                    alert(message);
                } else {
                    location.href = '/login';
                }
            });
        }
    }
})

