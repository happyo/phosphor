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
            location.href = href + 'new';
        }
    }
});
