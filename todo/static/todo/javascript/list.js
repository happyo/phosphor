var list = new Vue({
    el: '#todoList',
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
        }).then(function (response) {
            var data = response['data'];
            var code = data['code'];
            if (code == 0) {
                var message = data['data']['errorMessage'];
                alert(message);
            } else {
                this.items = data['data']['items'];
            }
        });
    }
})
