var list = new Vue({
    el: '#list',
    data: {
        items: []
    },

    mounted() {
        axios({
            method: 'get',
            url: '',
            headers: {
                'Accept':'application/json'
            }
        }).then(response => {
            var data = response['data'];
            var code = data['code'];
            if (code == 0) {
                var message = data['data']['errorMessage'];
                alert(message);
            } else {
                this.items = data['data']['items'];
                console.log(this.items[0]);
            }
        });
    },

    methods: {
        addItem: function (event) {
            var href = location.href;
            location.href = href + '/new';
        },
        editItem: function (todoId) {
            var href = location.href;
            console.log(href + '/' + todoId);
            location.href = href + '/' + todoId + '/';
        },
        finishItem: function (todoId) {
            var params = new URLSearchParams();
            params.append('status', 1);
            var requestUrl = location.href + '/' + todoId + '/';
            axios({
                method: 'put',
                url: requestUrl,
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
                    location.reload();
                }
            });
        },
        deleteItem: function (todoId) {
            var requestUrl = location.href + '/' + todoId + '/';
            axios({
                method: 'delete',
                url: requestUrl,
            }).then(function (response) {
                var data = response['data'];
                var code = data['code'];
                if (code == 0) {
                    var message = data['data']['errorMessage'];
                    alert(message);
                } else {
                    location.reload();
                }
            });
        }
    }
});
