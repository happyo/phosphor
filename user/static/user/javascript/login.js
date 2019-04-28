var user = new Vue({
    el: '#user',
    data: {
        username: '',
        password: ''
    },
    methods: {
        login: function (event) {
            apiSignIn({'username' : this.username, 'password' : this.password}).then(res => {
                var data = res['data'];
                var username = data['username'];
                location.href = '/' + username + '/todos';
            }).catch();
        },
        register: function (event) {
            location.href = '/join';
        }
    }
})
