// import axios from 'axios';
// import QS from 'qs';
// import { Toast } from 'vant';

axios.defaults.timeout = 10000;

axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';

// 响应拦截器
axios.interceptors.response.use(
    response => {
        if (response.status == 200) {
            var data = response['data'];
            var code = data['code'];

            if (code == 0) {
                var errorMessage = data['data']['errorMessage'];
                vant.Toast(errorMessage);

                return Promise.reject(response);
            } else {
                return Promise.resolve(response);
            }
        } else {
            return Promise.reject(response);
        }
    },
    error => {
        return Promise.reject(error.response);
    }
);

function getWithConfig(url, params, config) {
    return new Promise((resolve, reject) => {
        axios.get(url, {
            params: params,
        }, config).then(res => {
            resolve(res.data);
        }).catch(err => {
            reject(err.data);
        });
    });
}

function get(url, params) {
    return getWithConfig(url, params, {});
}

function getHTML(url, params) {
    return getWithConfig(url, params, {
        headers: {
            'accept':'application/json'
        }
    });
}

function post(url, params) {
    return new Promise(function (resolve, reject) {

        axios.post(url, Qs.stringify(params)).then(res => {
            resolve(res.data);
        }).catch(err => {
            reject(err.data);
        });

    });
}

function put(url, params) {
    return new Promise((resolve, reject) => {
        axios.put(url, Qs.stringify(params)).then(res => {
            resolve(res.data);
        }).catch(err => {
            reject(err.data);
        });
    });
}

function apiDelete(url) {
    return new Promise((resolve, reject) => {
        axios.delete(url).then(res => {
            resolve(res.data);
        }).catch(err => {
            reject(err.data);
        });
    });
}
