var todo = new Vue({
    el: '#todo',
    data: {
        title: '',
        detail: ''
    },
    methods: {
        add: function (event) {
            var params = new URLSearchParams();
            params.append('title', this.title);
            params.append('detail', this.detail);
            var parts = location.href.split('/');
            var lastSegment = parts.pop() || parts.pop();  // handle potential trailing slash
            var postUrl = parts.join('/');
            axios({
                method: 'post',
                url: postUrl,
                data: params,
                headers: {
                    'Content-Type':'application/x-www-form-urlencoded',
                    'Accept': 'application/json'
                }
            }).then(function (response) {
                var data = response['data'];
                var code = data['code'];
                if (code == 0) {
                    var message = data['data']['errorMessage'];
                    alert(message);
                } else {
                    location.href = postUrl;
                }
            });
        }
    }
})
