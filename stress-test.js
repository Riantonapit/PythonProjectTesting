import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
    stages: [
        { duration: '30s', target: 50 },   // Naik ke 50 user
        { duration: '1m', target: 100 },   // Bertahan di 100 user
        { duration: '30s', target: 0 },    // Turun ke 0 user
    ],
};

export default function () {
    // 1. Akses halaman login (GET)
    let res1 = http.get('https://dev.tixia.com/id');
    check(res1, {
        'login page status is 200': (r) => r.status === 200,
    });

    sleep(1);

    // 2. Submit form login (POST)
    let payload = JSON.stringify({
        email: 'testuser@example.com',
        password: 'password123'
    });

    let headers = { 'Content-Type': 'application/json' };
    let res2 = http.post('https://dev.tixia.com/id', payload, { headers: headers });

    check(res2, {
        'login success': (r) => r.status === 200 && r.json('token') !== '',
    });

    let token = res2.json('token');

    // 3. Akses dashboard setelah login
    let authHeaders = {
        headers: {
            Authorization: `Bearer ${token}`,
        },
    };

    let res3 = http.get('https://dev.tixia.com/api/dashboard', authHeaders);
    check(res3, {
        'dashboard status is 200': (r) => r.status === 200,
    });

    sleep(1);
}
