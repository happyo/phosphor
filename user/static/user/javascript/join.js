
var register = new Vue({
    el: '#register',
    data: {
        username: '',
        password: ''
    },
    methods: {
        join: function (event) {
            apiJoin({'username' : this.username, 'password' : this.password}).then(res => {
                location.href = '/login';
            });
        }
    }
})

