var user = new Vue({
    el: '#user',
    data: {
        username: '',
        password: ''
    },
    methods: {
        login: function (event) {
            var params = new URLSearchParams();
            params.append('username', this.username);
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
                    var username = data['data']['username'];
                    location.href = '/' + username + '/todos';
                }
            });
        }
    }
})
