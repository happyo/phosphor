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
            });
        }
    }
})
