var user = new Vue({
    el: '#user',
    data: {
        username: '',
        password: ''
    },
    methods: {
        login: function (event) {
            apiSignIn({'username' : this.username}).then(res => {
                var data = res['data'];
                var username = data['username'];
                location.href = '/' + username + '/todos';
            }).catch(err => {
            });
        },
        register: function (event) {
            location.href = '/join';
        }
    }
})
