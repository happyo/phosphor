var todo = new Vue({
    el: '#todo',
    data: {
        title: '',
        detail: ''
    },
    mounted () {

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
                this.title = data['data']['item']['title'];
                this.detail = data['data']['item']['detail'];
            }
        });

    },
    methods: {
        edit: function (event) {
            var params = new URLSearchParams();
            params.append('title', this.title);
            params.append('detail', this.detail);
            axios({
                method: 'put',
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
                    var parts = location.href.split('/');
                    var lastSegment = parts.pop() || parts.pop();  // handle potential trailing slash
                    location.href = parts.join('/');
                }
            });
        }
    }
})
