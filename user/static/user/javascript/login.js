var user = new Vue({
    el: '#user',
    data: {
        username: 'hah',
        password: '123'
    },
    methods: {
        login: function (event) {
            params = { 'username': this.username, 'password': this.password };
            axios.post('', { username: 'hahaha'}).then(function (response) {
                console.log(response);
                alert('success' + response);
            })
                .catch(function (error) {
                    console.log(error);
                });
        }
    }
})
